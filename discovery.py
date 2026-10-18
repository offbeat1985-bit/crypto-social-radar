"""Free DEX discovery: snapshots, anomaly scores, cautious identity and risk checks."""
import datetime as dt, json, math, os, sqlite3, urllib.request, urllib.parse, time
from pathlib import Path
DB=Path(__file__).resolve().parent/'data'/'radar.sqlite3'
HEAD={'User-Agent':'CryptoSocialRadarResearch/0.4','Accept':'application/json'}
def get(url,timeout=16):
 req=urllib.request.Request(url,headers=HEAD)
 with urllib.request.urlopen(req,timeout=timeout) as r:return json.load(r)
def init(c):
 c.executescript('''CREATE TABLE IF NOT EXISTS dex_snapshots(ts TEXT,chain TEXT,contract TEXT,pair TEXT,symbol TEXT,price REAL,liquidity REAL,volume24 REAL,buys24 INTEGER,sells24 INTEGER,age_hours REAL,source TEXT,PRIMARY KEY(ts,chain,contract));
 CREATE TABLE IF NOT EXISTS dex_discovery(ts TEXT,chain TEXT,contract TEXT,symbol TEXT,score REAL,status TEXT,reason TEXT,PRIMARY KEY(ts,chain,contract));
 CREATE TABLE IF NOT EXISTS dex_risks(day TEXT,chain TEXT,contract TEXT,status TEXT,detail TEXT,PRIMARY KEY(day,chain,contract));
 CREATE TABLE IF NOT EXISTS dex_source_runs(ts TEXT,source TEXT,status TEXT,items INTEGER,detail TEXT,PRIMARY KEY(ts,source));
 CREATE TABLE IF NOT EXISTS dex_provenance(ts TEXT,chain TEXT,contract TEXT,source TEXT,PRIMARY KEY(ts,chain,contract,source));''')
def mark(c,ts,source,status,count,detail=''):
 c.execute('INSERT OR REPLACE INTO dex_source_runs VALUES (?,?,?,?,?)',(ts,source,status,count,detail[:220]))
def pairs_from_dex():
 # Token discovery endpoints; follow each token to obtain actual trading pairs.
 results=[]
 for endpoint in ('https://api.dexscreener.com/token-profiles/latest/v1','https://api.dexscreener.com/token-boosts/latest/v1'):
  data=get(endpoint)
  if not isinstance(data,list):raise ValueError('unexpected DexScreener response')
  results.extend((x.get('chainId'),x.get('tokenAddress')) for x in data)
 return list(dict.fromkeys((a,b) for a,b in results if a and b))[:70]
def dex_pairs(chain,contract):
 url='https://api.dexscreener.com/token-pairs/v1/'+urllib.parse.quote(chain,safe='')+'/'+urllib.parse.quote(contract,safe='')
 data=get(url)
 return data if isinstance(data,list) else []
def gecko_pools():
 # Public GeckoTerminal API; no key. Fetch limited new pools from major chains.
 out=[]
 for network in ('eth','solana','base','bsc'):
  data=get(f'https://api.geckoterminal.com/api/v2/networks/{network}/new_pools?page=1')
  if not isinstance(data.get('data'),list):raise ValueError('unexpected GeckoTerminal response')
  for pool in data['data']:
   ident=(((pool.get('relationships') or {}).get('base_token') or {}).get('data') or {}).get('id','')
   if ident.startswith(network+'_'):
    out.append((network,ident[len(network)+1:]))
 return out
CHAIN={'eth':'ethereum','solana':'solana','base':'base','bsc':'bsc'}
def normalize(pair,chain,contract,ts):
 if not isinstance(pair,dict):return None
 base=pair.get('baseToken') or {}
 if str(base.get('address','')).lower()!=contract.lower():return None
 try:
  price=float(pair.get('priceUsd') or 0);liq=float((pair.get('liquidity') or {}).get('usd') or 0)
  vol=float((pair.get('volume') or {}).get('h24') or 0)
  tx=(pair.get('txns') or {}).get('h24') or {};buys=int(tx.get('buys') or 0);sells=int(tx.get('sells') or 0)
  created=pair.get('pairCreatedAt');age=(time.time()-float(created)/1000)/3600 if created else None
  if price<=0:return None
  return (ts,chain,contract.lower(),str(pair.get('pairAddress') or ''),str(base.get('symbol') or '?')[:30],price,liq,vol,buys,sells,age,'dexscreener')
 except (ValueError,TypeError,OverflowError):return None
def security(chain,contract):
 # GoPlus EVM token security; unsupported chains remain unverified, never 'safe'.
 ids={'ethereum':'1','base':'8453','bsc':'56'}
 if chain not in ids:return ('unverified','GoPlus chain unsupported in this integration')
 try:
  url=f'https://api.gopluslabs.io/api/v1/token_security/{ids[chain]}?contract_addresses='+urllib.parse.quote(contract)
  data=get(url);r=(data.get('result') or {}).get(contract.lower()) or {}
  if not r:return ('unverified','No GoPlus token result')
  bad=[k for k in ('is_honeypot','is_blacklisted','cannot_sell_all','is_proxy','hidden_owner') if str(r.get(k))=='1']
  if bad:return ('high_risk',','.join(bad))
  return ('unverified','No flagged fields in limited automated check; NOT a safety guarantee')
 except Exception as e:return ('unverified',f'GoPlus {type(e).__name__}: {str(e)[:100]}')
def run():
 ts=dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat();day=ts[:10]
 DB.parent.mkdir(exist_ok=True,parents=True);c=sqlite3.connect(DB);init(c)
 candidates=[]
 provenance={}
 for name,fn in [('dexscreener',pairs_from_dex),('geckoterminal',gecko_pools)]:
  try:
   rows=fn()
   for chain,contract in rows:
    key=(CHAIN.get(chain,chain),contract)
    candidates.append(key)
    provenance.setdefault((key[0],str(key[1]).lower()),set()).add(name)
   mark(c,ts,name,'ok',len(rows))
  except Exception as e:mark(c,ts,name,'error',0,f'{type(e).__name__}: {e}')
 # Keep previously forecast assets observable even if they disappear from trending feeds.
 if c.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='v41_predictions'").fetchone():
  tracked=c.execute('SELECT chain,contract FROM v41_predictions WHERE day>=? GROUP BY chain,contract ORDER BY max(day) DESC',((dt.datetime.now(dt.timezone.utc).date()-dt.timedelta(days=9)).isoformat(),)).fetchall()
  candidates=tracked+candidates
 candidates=list(dict.fromkeys((chain,contract) for chain,contract in candidates if chain and contract))
 tracked_count=len(tracked) if 'tracked' in locals() else 0
 if tracked_count>200:raise RuntimeError('More than 200 tracked assets: split scan into batches')
 candidates=candidates[:200]
 successes=0
 for chain,contract in candidates:
  try:
   pairs=dex_pairs(chain,contract)
   normalized=[normalize(p,chain,contract,ts) for p in pairs]
   normalized=[x for x in normalized if x]
   if not normalized:continue
   original=None
   if c.execute("SELECT 1 FROM sqlite_master WHERE name='v41_predictions'").fetchone():
    prev=c.execute('SELECT pair FROM v41_predictions WHERE chain=? AND contract=? ORDER BY observed_at LIMIT 1',(chain,contract.lower())).fetchone()
    if prev:original=prev[0]
   same=[x for x in normalized if x[3]==original] if original else []
   best=max(same or normalized,key=lambda x:x[6])
   c.execute('INSERT OR IGNORE INTO dex_snapshots VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',best)
   for source in provenance.get((chain,contract.lower()),()):
    c.execute('INSERT OR IGNORE INTO dex_provenance VALUES (?,?,?,?)',(ts,chain,contract.lower(),source))
   _,_,_,_,symbol,price,liq,vol,buys,sells,age,_=best
   old=c.execute('SELECT price,ts FROM dex_snapshots WHERE chain=? AND contract=? AND ts<? ORDER BY ts DESC LIMIT 1',(chain,contract.lower(),ts)).fetchone()
   momentum=(price/old[0]-1) if old and old[0]>0 and 2 <= (dt.datetime.fromisoformat(ts)-dt.datetime.fromisoformat(old[1])).total_seconds()/3600 <= 8 else None
   # Do not claim acceleration without a prior observation.
   score=round(min(100,25*math.log1p(vol/max(liq,1))+12*math.log1p(buys)+15*max(-1,min(1,momentum or 0))),1)
   status='watch_only';reason=[]
   if liq<20000:reason.append('liquidity below USD 20k')
   if vol<10000:reason.append('24h volume below USD 10k')
   if buys<20:reason.append('fewer than 20 buys in 24h')
   if momentum is None:reason.append('no comparable 2-8h prior price snapshot')
   elif momentum<0.03:reason.append('price change below +3% over observed 2-8h interval')
   if age is None:reason.append('pool age unknown')
   if not reason:status='candidate'
   if status=='candidate':
    risk,detail=security(chain,contract)
    c.execute('INSERT OR REPLACE INTO dex_risks VALUES (?,?,?,?,?)',(day,chain,contract.lower(),risk,detail))
    if risk=='high_risk':status='excluded';reason.append('GoPlus high-risk flag')
    elif risk=='unverified':status='needs_review';reason.append('security not independently verified')
   c.execute('INSERT OR REPLACE INTO dex_discovery VALUES (?,?,?,?,?,?,?)',(ts,chain,contract.lower(),symbol,score,status,'; '.join(reason) or 'quantitative thresholds met'))
   successes+=1
  except Exception as e:
   mark(c,ts,'pair:'+chain+':'+contract[:14],'error',0,f'{type(e).__name__}: {e}')
 mark(c,ts,'pair_collection','ok' if successes else 'empty',successes)
 c.commit();c.close();print(f'{ts}: {successes} DEX assets snapshotted; {len(candidates)} unique candidates')
if __name__=='__main__':run()
