"""Append a source-aware DEX research section to the existing weekly report."""
import datetime as dt,sqlite3
from pathlib import Path
ROOT=Path(__file__).resolve().parent;db=ROOT/'data/radar.sqlite3';report=ROOT/'reports/latest.md'
if not db.exists() or not report.exists():raise SystemExit('Database or weekly report missing')
c=sqlite3.connect(db)
if not c.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='dex_snapshots'").fetchone():
 print('No DEX collection yet; skipping report section');raise SystemExit(0)
cutoff=(dt.datetime.now(dt.timezone.utc)-dt.timedelta(days=7)).isoformat()
lines=['','## DEX discovery (experimental, not trading signals)','']
for source,status,count in c.execute('SELECT source,status,count(*) FROM dex_source_runs WHERE ts>=? GROUP BY source,status ORDER BY source,status',(cutoff,)):
 if source.startswith('pair:'):continue
 lines.append(f'- {source}: {status}, {count} runs')
count=c.execute('SELECT count(*) FROM dex_snapshots WHERE ts>=?',(cutoff,)).fetchone()[0]
lines.append(f'- Pair snapshots this week: {count}')
if c.execute("SELECT 1 FROM sqlite_master WHERE name='dex_provenance'").fetchone():
 for source,assets in c.execute('SELECT source,count(DISTINCT chain||":"||contract) FROM dex_provenance WHERE ts>=? GROUP BY source',(cutoff,)):
  lines.append(f'- Unique tokens from {source}: {assets}')
lines.append('- Discovery scores are exploratory, not calibrated probabilities. One 24h volume measurement is not a 4h volume measurement.')
lines.append('- Candidate and security statuses are NOT investment recommendations; unverified means unverified.')
rows=c.execute("SELECT ts,chain,symbol,score,status,reason FROM dex_discovery WHERE ts>=? AND status IN ('candidate','needs_review','excluded') ORDER BY ts DESC,score DESC LIMIT 15",(cutoff,)).fetchall()
if not rows:lines.append('- No eligible reviewed candidates yet.')
for ts,chain,symbol,score,status,reason in rows:lines.append(f'- {ts} {chain} {symbol}: {status}, score {score}; {reason}')
report.write_text(report.read_text(encoding='utf-8')+'\n'.join(lines)+'\n',encoding='utf-8')
