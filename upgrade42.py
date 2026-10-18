"""One-time v4.2 patch. Run in repository root; leaves SQLite history untouched."""
from pathlib import Path
import ast
root=Path(__file__).resolve().parent

def patch(name, old, new):
    f=root/name
    src=f.read_text()
    if old not in src:
        if new in src: return
        raise RuntimeError(f'{name}: source changed; manual review required')
    updated=src.replace(old,new)
    ast.parse(updated,filename=name)
    f.write_text(updated)
    print('Patched',name)

patch('discovery.py',"  out.extend((network,p['attributes'].get('base_token_address')) for p in data['data'] if p.get('attributes',{}).get('base_token_address'))", "  for pool in data['data']:\n   ident=(((pool.get('relationships') or {}).get('base_token') or {}).get('data') or {}).get('id','')\n   if ident.startswith(network+'_'):\n    out.append((network,ident[len(network)+1:]))")
patch('discovery.py', " CREATE TABLE IF NOT EXISTS dex_source_runs(ts TEXT,source TEXT,status TEXT,items INTEGER,detail TEXT,PRIMARY KEY(ts,source));", " CREATE TABLE IF NOT EXISTS dex_source_runs(ts TEXT,source TEXT,status TEXT,items INTEGER,detail TEXT,PRIMARY KEY(ts,source));\n CREATE TABLE IF NOT EXISTS dex_provenance(ts TEXT,chain TEXT,contract TEXT,source TEXT,PRIMARY KEY(ts,chain,contract,source));")
patch('discovery.py', " candidates=[]\n for name,fn in", " candidates=[]\n provenance={}\n for name,fn in")
patch('discovery.py', "   rows=fn();candidates.extend((CHAIN.get(chain,chain),contract) for chain,contract in rows)\n   mark(c,ts,name,'ok',len(rows))", "   rows=fn()\n   for chain,contract in rows:\n    key=(CHAIN.get(chain,chain),contract)\n    candidates.append(key)\n    provenance.setdefault((key[0],str(key[1]).lower()),set()).add(name)\n   mark(c,ts,name,'ok',len(rows))")
patch('discovery.py', 'ORDER BY max(day) DESC LIMIT 40', 'ORDER BY max(day) DESC')
patch('discovery.py', " candidates=list(dict.fromkeys((chain,contract) for chain,contract in candidates if chain and contract))[:100]", " candidates=list(dict.fromkeys((chain,contract) for chain,contract in candidates if chain and contract))\n tracked_count=len(tracked) if 'tracked' in locals() else 0\n if tracked_count>200:raise RuntimeError('More than 200 tracked assets: split scan into batches')\n candidates=candidates[:200]")
patch('discovery.py', "   best=max(normalized,key=lambda x:x[6]);c.execute('INSERT OR IGNORE INTO dex_snapshots VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',best)", "   original=None\n   if c.execute(\"SELECT 1 FROM sqlite_master WHERE name='v41_predictions'\").fetchone():\n    prev=c.execute('SELECT pair FROM v41_predictions WHERE chain=? AND contract=? ORDER BY observed_at LIMIT 1',(chain,contract.lower())).fetchone()\n    if prev:original=prev[0]\n   same=[x for x in normalized if x[3]==original] if original else []\n   best=max(same or normalized,key=lambda x:x[6])\n   c.execute('INSERT OR IGNORE INTO dex_snapshots VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',best)\n   for source in provenance.get((chain,contract.lower()),()):\n    c.execute('INSERT OR IGNORE INTO dex_provenance VALUES (?,?,?,?)',(ts,chain,contract.lower(),source))")
patch('validation41.py', "    if risk == 'high_risk': reasons.append('GoPlus high-risk finding')\n    elif risk != 'verified_low_risk': reasons.append('contract safety not independently verified')\n    b = 'rejected' if risk == 'high_risk' else ('supported' if not reasons else 'unconfirmed')", "    if risk == 'high_risk': reasons.append('GoPlus high-risk finding')\n    elif risk != 'verified_low_risk': reasons.append('contract safety unverified; separate from market assessment')\n    market_ok = liq >= 100000 and buys+sells >= 100 and age is not None and age >= 24\n    b = 'rejected' if risk == 'high_risk' else ('supported_market_only' if market_ok else 'unconfirmed')")
patch('validation41.py', "'v4.1-frozen-1'))", "'v4.2-market-review-1'))")
patch('validation41.py', "'- Agent B independently records supported/unconfirmed/rejected; unverified security is not treated as safe.'", "'- Agent B market-only support does not mean contract safety; unverified remains unverified.'")
patch('dex_report.py', "lines.append(f'- Pair snapshots this week: {count}')", "lines.append(f'- Pair snapshots this week: {count}')\nif c.execute(\"SELECT 1 FROM sqlite_master WHERE name='dex_provenance'\").fetchone():\n for source,assets in c.execute('SELECT source,count(DISTINCT chain||\":\"||contract) FROM dex_provenance WHERE ts>=? GROUP BY source',(cutoff,)):\n  lines.append(f'- Unique tokens from {source}: {assets}')")
print('v4.2 patch complete; prior predictions and database preserved')
