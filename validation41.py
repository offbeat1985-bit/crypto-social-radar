"""V4.1 forward-only shadow evaluation of DEX discovery; no trading or self-training.

Uses standard library and existing SQLite database. Never edits earlier predictions.
"""
import argparse
import datetime as dt
import hashlib
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = ROOT / 'data' / 'radar.sqlite3'
UTC = dt.timezone.utc
HORIZONS = (1, 3, 7)


def setup(c):
    c.executescript('''
    CREATE TABLE IF NOT EXISTS v41_predictions (
      prediction_id TEXT PRIMARY KEY, observed_at TEXT NOT NULL,
      day TEXT NOT NULL, chain TEXT NOT NULL, contract TEXT NOT NULL,
      pair TEXT NOT NULL, symbol TEXT NOT NULL, entry_price REAL NOT NULL,
      liquidity REAL NOT NULL, volume24 REAL NOT NULL,
      buys24 INTEGER NOT NULL, sells24 INTEGER NOT NULL,
      age_hours REAL, agent_a TEXT NOT NULL, agent_b TEXT NOT NULL,
      a_reason TEXT NOT NULL, b_reason TEXT NOT NULL,
      cohort TEXT NOT NULL, model_version TEXT NOT NULL);
    CREATE UNIQUE INDEX IF NOT EXISTS v41_one_asset_per_day
      ON v41_predictions(day,chain,contract);
    CREATE TABLE IF NOT EXISTS v41_outcomes (
      prediction_id TEXT NOT NULL, horizon INTEGER NOT NULL,
      observed_at TEXT NOT NULL, exit_price REAL NOT NULL,
      return_pct REAL NOT NULL, PRIMARY KEY(prediction_id,horizon));
    CREATE TABLE IF NOT EXISTS v41_evaluation_status (
      prediction_id TEXT NOT NULL, horizon INTEGER NOT NULL,
      status TEXT NOT NULL, detail TEXT NOT NULL, checked_at TEXT NOT NULL,
      PRIMARY KEY(prediction_id,horizon));
    ''')


def parse_ts(value):
    return dt.datetime.fromisoformat(value.replace('Z', '+00:00')).astimezone(UTC)


def assess(liq, vol, buys, sells, age, risk):
    # Frozen and explainable rules. 24h totals are NOT called 4h acceleration.
    a_good = liq >= 50000 and vol >= 25000 and buys >= 30 and buys >= sells * 1.3
    a = 'candidate' if a_good else 'watch_only'
    ar = f'liq={liq:.0f}, 24h_volume={vol:.0f}, 24h_buys={buys}, 24h_sells={sells}; thresholds frozen v4.1'
    # Independent risk/liquidity review, not dependent on Agent A score.
    reasons = []
    if liq < 100000: reasons.append('liquidity below USD 100k')
    if buys + sells < 100: reasons.append('fewer than 100 transactions in 24h')
    if age is None or age < 24: reasons.append('pool age under 24h or unknown')
    if risk == 'high_risk': reasons.append('GoPlus high-risk finding')
    elif risk != 'verified_low_risk': reasons.append('contract safety unverified; separate from market assessment')
    market_ok = liq >= 100000 and buys+sells >= 100 and age is not None and age >= 24
    b = 'rejected' if risk == 'high_risk' else ('supported_market_only' if market_ok else 'unconfirmed')
    return a, b, ar, '; '.join(reasons) or 'passed defined review checks'


def collect(c):
    setup(c)
    # Only latest collection batch, never reinterpret historic batches as fresh forecasts.
    latest = c.execute('SELECT MAX(ts) FROM dex_snapshots').fetchone()[0]
    if not latest: return 0
    day = latest[:10]
    rows = c.execute('''SELECT s.ts,s.chain,s.contract,s.pair,s.symbol,s.price,
       s.liquidity,s.volume24,s.buys24,s.sells24,s.age_hours,
       COALESCE(r.status,'unverified')
       FROM dex_snapshots s LEFT JOIN dex_risks r
       ON r.day=? AND r.chain=s.chain AND r.contract=s.contract
       WHERE s.ts=? ORDER BY s.chain,s.contract''', (day,latest)).fetchall()
    n = 0
    for ts,chain,contract,pair,symbol,price,liq,vol,buys,sells,age,risk in rows:
        if not pair or not price or price <= 0 or liq is None or liq < 20000: continue
        # Ignore repeats on same UTC date; first observed snapshot fixes entry.
        if c.execute('SELECT 1 FROM v41_predictions WHERE day=? AND chain=? AND contract=?',
                     (day,chain,contract)).fetchone(): continue
        a,b,ar,br = assess(liq,vol,buys,sells,age,risk)
        # A deterministic control group from eligible non-candidates, selected ex ante.
        control = int(hashlib.sha256(f'{day}:{chain}:{contract}'.encode()).hexdigest()[:8],16) % 5 == 0
        if a != 'candidate' and not control: continue
        cohort = 'signal' if a == 'candidate' else 'control'
        pid = hashlib.sha256(f'v4.1|{day}|{chain}|{contract}'.encode()).hexdigest()
        c.execute('''INSERT OR IGNORE INTO v41_predictions VALUES
          (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
          (pid,ts,day,chain,contract,pair,symbol,price,liq,vol,buys,sells,age,
           a,b,ar,br,cohort,'v4.2-market-review-1'))
        n += 1
    return n


def evaluate(c, at=None):
    setup(c)
    now = at or dt.datetime.now(UTC)
    n = 0
    for pid,started,chain,contract,pair,entry in c.execute('''
        SELECT prediction_id,observed_at,chain,contract,pair,entry_price
        FROM v41_predictions''').fetchall():
        start = parse_ts(started)
        for horizon in HORIZONS:
            if c.execute('SELECT 1 FROM v41_outcomes WHERE prediction_id=? AND horizon=?',(pid,horizon)).fetchone(): continue
            target = start + dt.timedelta(days=horizon)
            if now < target + dt.timedelta(hours=6): continue
            # The closest observed snapshot within six hours after target.
            end = c.execute('''SELECT ts,price FROM dex_snapshots
                WHERE chain=? AND contract=? AND pair=? AND ts>=? AND ts<=?
                ORDER BY ts LIMIT 1''',
                (chain,contract,pair,target.isoformat(),(target+dt.timedelta(hours=6)).isoformat())).fetchone()
            if end and end[1] > 0:
                c.execute('INSERT OR IGNORE INTO v41_outcomes VALUES (?,?,?,?,?)',
                          (pid,horizon,end[0],end[1],(end[1]/entry-1)*100))
                c.execute('DELETE FROM v41_evaluation_status WHERE prediction_id=? AND horizon=?',(pid,horizon))
                n += 1
            else:
                # Explicitly track missing/delisted/changed-pair outcomes, never silently drop.
                c.execute('INSERT OR REPLACE INTO v41_evaluation_status VALUES (?,?,?,?,?)',
                          (pid,horizon,'missing','No same-pair quote within 6h after target; not a zero return',now.isoformat()))
    return n


def report(c):
    setup(c)
    lines = ['','## V4.1 forward-only shadow evaluation (frozen rules)','',
             '- Not financial advice; no orders, no automatic weight changes.',
             '- First observation per asset per UTC day; outcomes use same DEX pair and 1/3/7-day targets.',
             '- Controls are a deterministic 20% sample of eligible watch-only assets, not matched random controls.',
             '- Missing quotes and delistings are separately counted; ignoring them biases returns upward.',
             '- 24h volume is a rolling 24h measure, not a four-hour acceleration measure.']
    n=c.execute('SELECT count(*) FROM v41_predictions').fetchone()[0]
    lines.append(f'- Frozen predictions: {n}')
    for cohort in ('signal','control'):
        total=c.execute('SELECT count(*) FROM v41_predictions WHERE cohort=?',(cohort,)).fetchone()[0]
        lines.append(f'- {cohort} cohort: {total} predictions')
        for h in HORIZONS:
            count,avg,positive=c.execute('''SELECT count(*),avg(o.return_pct),
              avg(CASE WHEN o.return_pct>0 THEN 1.0 ELSE 0.0 END)
              FROM v41_outcomes o JOIN v41_predictions p ON p.prediction_id=o.prediction_id
              WHERE p.cohort=? AND o.horizon=?''',(cohort,h)).fetchone()
            missing=c.execute('''SELECT count(*) FROM v41_evaluation_status e
              JOIN v41_predictions p ON p.prediction_id=e.prediction_id
              WHERE p.cohort=? AND e.horizon=? AND e.status='missing' ''',(cohort,h)).fetchone()[0]
            lines.append(f'  - {h}d: evaluated={count}; missing={missing}; '+
                         (f'mean={avg:+.2f}%; positive={positive*100:.1f}%' if count else 'insufficient observations'))
    lines.append('- Agent B market-only support does not mean contract safety; unverified remains unverified.')
    for a,b,n in c.execute('SELECT agent_a,agent_b,count(*) FROM v41_predictions GROUP BY agent_a,agent_b ORDER BY count(*) DESC'):
        lines.append(f'- Agent A {a} / Agent B {b}: {n}')
    return '\n'.join(lines)+'\n'


def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['collect','report']);args=p.parse_args()
    if not DB.exists(): raise SystemExit('Missing data/radar.sqlite3: run discovery first')
    with sqlite3.connect(DB) as c:
        setup(c)
        if args.mode=='collect':
            if not c.execute("SELECT 1 FROM sqlite_master WHERE name='dex_snapshots'").fetchone():
                raise SystemExit('Missing DEX snapshots table: run discovery first')
            n=collect(c);evaluated=evaluate(c);c.commit()
            print(f'v4.1: {n} new immutable predictions, {evaluated} evaluated outcomes')
        else:
            text=report(c)
            out=ROOT/'reports/latest.md'
            if not out.exists():raise SystemExit('Missing reports/latest.md')
            out.write_text(out.read_text(encoding='utf-8')+text,encoding='utf-8')
            print(text)

if __name__=='__main__':main()
