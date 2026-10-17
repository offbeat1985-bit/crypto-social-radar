"""Forward-only price snapshots and evaluation. No trading, no invented history."""
import datetime as dt, json, os, urllib.request

def setup(c):
 c.executescript("""CREATE TABLE IF NOT EXISTS price_snapshots(day TEXT,coin_id TEXT,symbol TEXT,price REAL,PRIMARY KEY(day,coin_id));
 CREATE TABLE IF NOT EXISTS predictions(day TEXT,asset TEXT,coin_id TEXT,agent_a TEXT,agent_b TEXT,entry REAL,PRIMARY KEY(day,asset));
 CREATE TABLE IF NOT EXISTS evaluations(day TEXT,asset TEXT,horizon INT,observed_day TEXT,change_pct REAL,btc_change_pct REAL,excess_pct REAL,agent_a TEXT,agent_b TEXT,PRIMARY KEY(day,asset,horizon));
 CREATE TABLE IF NOT EXISTS quality_runs(day TEXT PRIMARY KEY,status TEXT,detail TEXT);""")

def collect(c,day):
 setup(c)
 url='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
 headers={'User-Agent':'CryptoSocialRadarResearch/0.2','Accept':'application/json'}
 key=os.getenv('COINGECKO_DEMO_API_KEY','').strip()
 if key:headers['x-cg-demo-api-key']=key
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=25) as response:coins=json.load(response)
  valid=[]
  for x in coins:
   try:
    coin_id=str(x['id']);symbol=str(x['symbol']).upper();price=float(x['current_price'])
    if price>0:valid.append((day,coin_id,symbol,price))
   except (KeyError,ValueError,TypeError):pass
  if not valid:raise ValueError('No valid prices received')
  c.executemany('INSERT OR IGNORE INTO price_snapshots VALUES (?,?,?,?)',valid)
  symbols={}
  for _,coin_id,symbol,price in valid:symbols.setdefault(symbol,[]).append((coin_id,price))
  rows=c.execute('SELECT s.asset,s.verdict,a.final_verdict FROM signals s JOIN audits a ON s.day=a.day AND s.asset=a.asset WHERE s.day=?',(day,)).fetchall()
  for asset,a,b in rows:
   matches=symbols.get(asset,[])
   if len(matches)==1:
    coin_id,price=matches[0]
    c.execute('INSERT OR IGNORE INTO predictions VALUES (?,?,?,?,?,?)',(day,asset,coin_id,a,b,price))
  c.execute('INSERT OR REPLACE INTO quality_runs VALUES (?,?,?)',(day,'ok',f'{len(valid)} coin prices; {len(rows)} signal assets'))
 except Exception as e:
  c.execute('INSERT OR REPLACE INTO quality_runs VALUES (?,?,?)',(day,'error',f'{type(e).__name__}: {str(e)[:180]}'))
 evaluate(c,day)
 c.commit()

def evaluate(c,today):
 setup(c)
 for day,asset,coin_id,a,b,entry in c.execute('SELECT * FROM predictions').fetchall():
  start=dt.date.fromisoformat(day)
  btc0=c.execute("SELECT price FROM price_snapshots WHERE day=? AND coin_id='bitcoin'",(day,)).fetchone()
  for h in (1,3,7):
   if (dt.date.fromisoformat(today)-start).days<h:continue
   if c.execute('SELECT 1 FROM evaluations WHERE day=? AND asset=? AND horizon=?',(day,asset,h)).fetchone():continue
   target=(start+dt.timedelta(days=h)).isoformat();last=(start+dt.timedelta(days=h+1)).isoformat()
   end=c.execute('SELECT day,price FROM price_snapshots WHERE coin_id=? AND day>=? AND day<=? ORDER BY day LIMIT 1',(coin_id,target,last)).fetchone()
   if not end:continue
   observed,price=end
   btcend=c.execute("SELECT price FROM price_snapshots WHERE day=? AND coin_id='bitcoin'",(observed,)).fetchone()
   btc=(btcend[0]/btc0[0]-1)*100 if btc0 and btcend and btc0[0]>0 else None
   change=(price/entry-1)*100
   c.execute('INSERT OR IGNORE INTO evaluations VALUES (?,?,?,?,?,?,?,?,?)',(day,asset,h,observed,change,btc,change-btc if btc is not None else None,a,b))

def report(c):
 setup(c)
 lines=['','## Forward-only price validation','']
 latest=c.execute('SELECT day,status,detail FROM quality_runs ORDER BY day DESC LIMIT 1').fetchone()
 lines.append(f'- Latest price feed: {latest[0]} / {latest[1]} / {latest[2]}' if latest else '- Price feed not run')
 lines.append(f"- Saved price snapshots: {c.execute('SELECT count(*) FROM price_snapshots').fetchone()[0]}")
 lines.append(f"- Matched asset predictions: {c.execute('SELECT count(*) FROM predictions').fetchone()[0]}")
 lines.append('- Only uniquely matched CoinGecko top-100 symbols are evaluated; no backfilled entries.')
 for h in (1,3,7):
  lines.append(f'### {h}-day validation')
  for name,where in [('Agent A candidates',"agent_a='candidate'"),('Agent B supported',"agent_b='review'"),('Agent A rejected by B',"agent_a='candidate' AND agent_b!='review'")]:
   n,mean,excess,hits=c.execute(f'SELECT count(*),avg(change_pct),avg(excess_pct),avg(CASE WHEN change_pct>0 THEN 1.0 ELSE 0.0 END) FROM evaluations WHERE horizon=? AND {where}',(h,)).fetchone()
   lines.append(f'- {name}: n={n}; positive={hits*100:.1f}%; average={mean:+.2f}%; excess vs BTC={excess:+.2f}%' if n and excess is not None else f'- {name}: n={n}; insufficient observations or BTC benchmark')
 lines.append('Scores are not probabilities. BTC is a benchmark, not a matched random-signal control. Small samples cannot establish predictive skill.')
 return '\n'.join(lines)+'\n'
