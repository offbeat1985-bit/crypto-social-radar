"""Free, standard-library-only social signal research prototype. No trading."""
import argparse, collections, datetime as dt, email.utils, hashlib, html, json, math, os, re, sqlite3, urllib.request, urllib.parse, xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB=ROOT/'data'/'radar.sqlite3'
FEEDS=[('reddit_cryptocurrency','https://www.reddit.com/r/CryptoCurrency/.rss'),('reddit_memecoins','https://www.reddit.com/r/memecoins/.rss'),('reddit_cryptomoonshots','https://www.reddit.com/r/CryptoMoonShots/.rss'),('google_news','https://news.google.com/rss/search?q=cryptocurrency+memecoin+token+launch&hl=en-US&gl=US&ceid=US:en')]
POS=('launch','listing','partnership','adoption','viral','breakout','community','airdrop','trending','growth','milestone')
NEG=('scam','rug','hack','exploit','fraud','dump','warning','lawsuit','phishing','honeypot')
STOP={'BTC','ETH','USD','USDT','USDC','NFT','AI','CEO','SEC','ETF','DEX','CEX','FOMO','DYOR','SOL','XRP'}
CASHTAG=re.compile(r'(?<!\w)\$([A-Za-z][A-Za-z0-9]{1,11})\b')
CONTRACT=re.compile(r'\b0x[a-fA-F0-9]{40}\b')

def now():return dt.datetime.now(dt.timezone.utc).isoformat()
def connect():
 DB.parent.mkdir(parents=True,exist_ok=True); c=sqlite3.connect(DB)
 c.executescript('''CREATE TABLE IF NOT EXISTS posts(id TEXT PRIMARY KEY, source TEXT, published TEXT, title TEXT, link TEXT, content TEXT, collected TEXT);
 CREATE TABLE IF NOT EXISTS signals(day TEXT, asset TEXT, score REAL, bullish REAL, risk REAL, mentions INT, sources INT, verdict TEXT, rationale TEXT, PRIMARY KEY(day,asset));
 CREATE TABLE IF NOT EXISTS audits(day TEXT,asset TEXT, independent_score REAL, independent_verdict TEXT, objections TEXT, final_verdict TEXT, PRIMARY KEY(day,asset));
 CREATE TABLE IF NOT EXISTS runs(day TEXT PRIMARY KEY, fetched INT, errors TEXT, timestamp TEXT);
 CREATE TABLE IF NOT EXISTS outcomes(day TEXT,asset TEXT,horizon INT,change_pct REAL,verified_at TEXT,source TEXT, PRIMARY KEY(day,asset,horizon));''')
 return c

def fetch(source,url):
 req=urllib.request.Request(url,headers={'User-Agent':'SocialRadarResearch/0.1 (public RSS, no automation of trades)'})
 with urllib.request.urlopen(req,timeout=18) as response: body=response.read(2_000_000)
 root=ET.fromstring(body); rows=[]
 for e in root.findall('.//item')+root.findall('.//{http://www.w3.org/2005/Atom}entry'):
  def field(tag):
   x=e.find(tag);return ''.join(x.itertext()).strip() if x is not None else ''
  title=html.unescape(re.sub('<[^>]*>',' ',field('title') or field('{http://www.w3.org/2005/Atom}title')))
  content=html.unescape(re.sub('<[^>]*>',' ',field('description') or field('{http://www.w3.org/2005/Atom}content')))
  link=field('link'); atomlink=e.find('{http://www.w3.org/2005/Atom}link')
  if not link and atomlink is not None:link=atomlink.get('href','')
  published=field('pubDate') or field('{http://www.w3.org/2005/Atom}updated') or now()
  try:
   date=email.utils.parsedate_to_datetime(published).astimezone(dt.timezone.utc).isoformat() if ',' in published else dt.datetime.fromisoformat(published.replace('Z','+00:00')).isoformat()
  except (ValueError,TypeError):date=now()
  uid=hashlib.sha256((source+'|'+link+'|'+title).encode()).hexdigest()
  rows.append((uid,source,date,title,link,content[:2500],now()))
 return rows

def tokens(text):
 found={x.upper() for x in CASHTAG.findall(text) if x.upper() not in STOP}
 found.update('ETH:'+x.lower() for x in CONTRACT.findall(text))
 return found

def analyze(c,day):
 # Only posts from last 48h, avoid treating historical reposts as new signals.
 cutoff=(dt.datetime.now(dt.timezone.utc)-dt.timedelta(hours=48)).isoformat()
 rows=c.execute('SELECT source,title,content,link,published FROM posts WHERE published>=?',(cutoff,)).fetchall()
 assets=collections.defaultdict(list)
 for source,title,content,link,published in rows:
  for token in tokens(title+' '+content):assets[token].append((source,title,content,link,published))
 count=0
 for asset,posts in assets.items():
  mentions=len(posts); sources=len(set(p[0] for p in posts))
  # Agent A: conservative explainable ranking, not calibrated probabilities.
  positive=sum(any(w in (p[1]+' '+p[2]).lower() for w in POS) for p in posts)
  negative=sum(any(w in (p[1]+' '+p[2]).lower() for w in NEG) for p in posts)
  score=min(100,round(18*math.log1p(mentions)+14*(sources-1)+5*positive,1))
  bullish=round(100*positive/max(1,positive+negative+2),1)
  risk=round(min(100, 25+15*(sources==1)+min(40,10*negative)+20*(mentions<3)),1)
  verdict='candidate' if mentions>=3 and sources>=2 and score>=60 else 'watch_only'
  rationale=f'{mentions} RSS mentions across {sources} sources; {positive} positive keyword hits, {negative} negative keyword hits. Cashtag/contract match is unverified.'
  c.execute('INSERT OR REPLACE INTO signals VALUES (?,?,?,?,?,?,?,?,?)',(day,asset,score,bullish,risk,mentions,sources,verdict,rationale))
  # Agent B: separate adversarial rules, does not use Agent A score for its own verdict.
  objections=[]
  if sources<2:objections.append('Only one source; no independent cross-community corroboration.')
  if mentions<5:objections.append('Very small sample.')
  if negative>0:objections.append('Negative or scam-related wording detected; sentiment may be misclassified.')
  if not asset.startswith('ETH:'):objections.append('Ticker collision possible; token identity not verified by contract.')
  if positive==0:objections.append('No specific positive catalyst detected.')
  independent=min(100,round(mentions*7+sources*12-negative*15,1))
  independent_verdict='supported' if sources>=2 and mentions>=5 and negative==0 and asset.startswith('ETH:') else 'insufficient_evidence'
  final='review' if verdict=='candidate' and independent_verdict=='supported' else 'unconfirmed'
  c.execute('INSERT OR REPLACE INTO audits VALUES (?,?,?,?,?,?)',(day,asset,independent,independent_verdict,' '.join(objections) or 'No automatic objections.',final))
  count+=1
 return count

def daily():
 day=dt.datetime.now(dt.timezone.utc).date().isoformat();c=connect(); fetched=0;errors=[]
 for source,url in FEEDS:
  try:
   posts=fetch(source,url);fetched+=len(posts)
   c.executemany('INSERT OR IGNORE INTO posts VALUES (?,?,?,?,?,?,?)',posts)
  except Exception as exc:errors.append(f'{source}: {type(exc).__name__}: {str(exc)[:120]}')
 if not fetched and not c.execute('SELECT 1 FROM posts LIMIT 1').fetchone():
  c.execute('INSERT OR REPLACE INTO runs VALUES (?,?,?,?)',(day,0,json.dumps(errors),now()));c.commit();raise RuntimeError('No source data available; cannot issue predictions')
 count=analyze(c,day)
 c.execute('INSERT OR REPLACE INTO runs VALUES (?,?,?,?)',(day,fetched,json.dumps(errors),now()));c.commit()
 print(f'{day}: fetched {fetched}, analyzed {count} assets, source errors {len(errors)}')
 c.close()

def weekly():
 c=connect();today=dt.datetime.now(dt.timezone.utc).date();start=(today-dt.timedelta(days=7)).isoformat()
 rows=c.execute('SELECT s.day,s.asset,s.score,s.mentions,s.sources,a.final_verdict,a.objections FROM signals s JOIN audits a ON (s.day=a.day AND s.asset=a.asset) WHERE s.day>=? AND s.verdict="candidate" ORDER BY s.day DESC,s.score DESC',(start,)).fetchall()
 runs=c.execute('SELECT day,fetched,errors FROM runs WHERE day>=? ORDER BY day',(start,)).fetchall()
 checked=c.execute('SELECT count(*) FROM outcomes WHERE day>=?',(start,)).fetchone()[0]
 lines=['# Weekly Social Radar Research Report',f'Period: {start} to {today.isoformat()} (UTC)','',f'- Daily collection runs: {len(runs)}/7 (scheduled; may be delayed or skipped)',f'- Candidate-day signals: {len(rows)}',f'- Independently supported signals: {sum(x[5]=="review" for x in rows)}',f'- Verified 1/3/7-day price outcomes: {checked}', '- **Forecast quality: NOT MEASURABLE until verified outcome data and baselines are available.**','- No trading. Scores are not probabilities.','']
 errors=[f'{day}: {err}' for day,n,err in runs if err and err!='[]']
 if errors:lines+=['## Collection limitations']+['- '+x for x in errors]+['']
 lines+=['## Signals and adversarial checks']
 if not rows:lines+=['No qualifying signals recorded.']
 for day,asset,score,mentions,sources,verdict,objections in rows[:25]:
  lines.append(f'- {day} **{asset}**: score {score}, {mentions} mentions, {sources} sources; reviewer: **{verdict}**. {objections}')
 lines+=['','## Model improvement proposals','- Increase verified source coverage before changing scoring weights.','- Add contract-level token disambiguation and historical backtesting.','- Maintain a frozen baseline and evaluate changes only on subsequent unseen data.','','## Important caveats','- Public RSS does not cover all coins or all social media.','- No historical price data ingestion is included, so this version cannot demonstrate profitable prediction.','- A GitHub scheduled job is not guaranteed to run at the exact time; free quotas and platform terms may change.']
 report='\n'.join(lines)+'\n';out=ROOT/'reports'/'latest.md';out.parent.mkdir(exist_ok=True);out.write_text(report,encoding='utf-8');print(report)
 c.close()

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['daily','weekly']);args=parser.parse_args()
 daily() if args.mode=='daily' else weekly()
