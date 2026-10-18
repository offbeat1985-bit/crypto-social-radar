# Weekly Social Radar Research Report
Period: 2026-10-11 to 2026-10-18 (UTC)

- Daily collection runs: 2/7 (scheduled; may be delayed or skipped)
- Candidate-day signals: 0
- Independently supported signals: 0
- Verified 1/3/7-day price outcomes: 0
- **Forecast quality: see forward-only price validation below; no skill claim without adequate samples and controls.**
- No trading. Scores are not probabilities.

## Collection limitations
- 2026-10-17: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-10-18: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]

## Source health and coverage
- coindesk: ok, 25 items
- cointelegraph: ok, 30 items
- decrypt: ok, 37 items
- google_news: ok, 100 items
- reddit_cryptocurrency: ok, 25 items
- reddit_cryptomoonshots: error, 0 items (HTTPError: HTTP Error 429: Too Many Requests)
- reddit_memecoins: error, 0 items (HTTPError: HTTP Error 429: Too Many Requests)

## Signals and adversarial checks
No qualifying signals recorded.

## Model improvement proposals
- Increase verified source coverage before changing scoring weights.
- Add contract-level token disambiguation and historical backtesting.
- Maintain a frozen baseline and evaluate changes only on subsequent unseen data.

## Important caveats
- Public RSS does not cover all coins or all social media.
- No historical price data ingestion is included, so this version cannot demonstrate profitable prediction.
- A GitHub scheduled job is not guaranteed to run at the exact time; free quotas and platform terms may change.

## Forward-only price validation

- Latest price feed: 2026-10-18 / ok / coingecko: 100 coin prices; 1 signal assets; 0 DEX contracts
- Saved price snapshots: 200
- Matched asset predictions: 0
- Top-100 ticker matches or Ethereum contract-address DEX matches only; no backfilled entries. CoinPaprika is an outage fallback, not an interchangeable historical ID.
### 1-day validation
- Agent A candidates: n=0; insufficient observations or BTC benchmark
- Agent B supported: n=0; insufficient observations or BTC benchmark
- Agent A rejected by B: n=0; insufficient observations or BTC benchmark
### 3-day validation
- Agent A candidates: n=0; insufficient observations or BTC benchmark
- Agent B supported: n=0; insufficient observations or BTC benchmark
- Agent A rejected by B: n=0; insufficient observations or BTC benchmark
### 7-day validation
- Agent A candidates: n=0; insufficient observations or BTC benchmark
- Agent B supported: n=0; insufficient observations or BTC benchmark
- Agent A rejected by B: n=0; insufficient observations or BTC benchmark
Scores are not probabilities. BTC is a benchmark, not a matched random-signal control. Small samples cannot establish predictive skill.


## DEX discovery (experimental, not trading signals)

- dexscreener: ok, 7 runs
- geckoterminal: ok, 7 runs
- pair_collection: ok, 7 runs
- Pair snapshots this week: 470
- Discovery scores are exploratory, not calibrated probabilities. One 24h volume measurement is not a 4h volume measurement.
- Candidate and security statuses are NOT investment recommendations; unverified means unverified.
- 2026-10-18T08:50:38+00:00 solana CBUCKS: needs_review, score 100.0; security not independently verified
- 2026-10-18T08:50:38+00:00 solana ELON: needs_review, score 100.0; security not independently verified
- 2026-10-18T08:50:38+00:00 solana iMolest : needs_review, score 100.0; security not independently verified
- 2026-10-18T08:50:38+00:00 solana CAPE: needs_review, score 100.0; security not independently verified
- 2026-10-18T08:50:38+00:00 solana MINTER: needs_review, score 100.0; security not independently verified
- 2026-10-18T08:50:38+00:00 robinhood SURPLUS: needs_review, score 100.0; security not independently verified
- 2026-10-18T08:50:38+00:00 robinhood OWN: needs_review, score 100.0; security not independently verified
- 2026-10-18T08:50:38+00:00 ethereum CLAUDIA: needs_review, score 100.0; security not independently verified
- 2026-10-18T08:50:38+00:00 bsc DAWG: needs_review, score 100.0; security not independently verified
- 2026-10-18T08:50:38+00:00 bsc priceless: needs_review, score 100.0; security not independently verified
- 2026-10-18T04:52:26+00:00 solana YILONGMA: needs_review, score 100.0; security not independently verified
- 2026-10-18T04:52:26+00:00 solana GLITCH: needs_review, score 100.0; security not independently verified
- 2026-10-18T04:52:26+00:00 solana Chaton: needs_review, score 100.0; security not independently verified
- 2026-10-18T04:52:26+00:00 solana STATE?: needs_review, score 100.0; security not independently verified
- 2026-10-18T04:52:26+00:00 solana FTR: needs_review, score 100.0; security not independently verified

## V4.1 forward-only shadow evaluation (frozen rules)

- Not financial advice; no orders, no automatic weight changes.
- First observation per asset per UTC day; outcomes use same DEX pair and 1/3/7-day targets.
- Controls are a deterministic 20% sample of eligible watch-only assets, not matched random controls.
- Missing quotes and delistings are separately counted; ignoring them biases returns upward.
- 24h volume is a rolling 24h measure, not a four-hour acceleration measure.
- Frozen predictions: 42
- signal cohort: 30 predictions
  - 1d: evaluated=0; missing=0; insufficient observations
  - 3d: evaluated=0; missing=0; insufficient observations
  - 7d: evaluated=0; missing=0; insufficient observations
- control cohort: 12 predictions
  - 1d: evaluated=0; missing=0; insufficient observations
  - 3d: evaluated=0; missing=0; insufficient observations
  - 7d: evaluated=0; missing=0; insufficient observations
- Agent B independently records supported/unconfirmed/rejected; unverified security is not treated as safe.
- Agent A candidate / Agent B unconfirmed: 30
- Agent A watch_only / Agent B unconfirmed: 12
