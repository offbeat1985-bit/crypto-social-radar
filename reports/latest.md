# Weekly Social Radar Research Report
Period: 2026-11-08 to 2026-11-15 (UTC)

- Daily collection runs: 7/7 (scheduled; may be delayed or skipped)
- Candidate-day signals: 0
- Independently supported signals: 0
- Verified 1/3/7-day price outcomes: 0
- **Forecast quality: see forward-only price validation below; no skill claim without adequate samples and controls.**
- No trading. Scores are not probabilities.

## Collection limitations
- 2026-11-08: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-09: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-10: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-11: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-12: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-13: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-14: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]

## Source health and coverage

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

- Latest price feed: 2026-11-14 / ok / coingecko: 100 coin prices; 0 signal assets; 0 DEX contracts
- Saved price snapshots: 2900
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

- dexscreener: ok, 36 runs
- geckoterminal: ok, 36 runs
- pair_collection: ok, 36 runs
- Pair snapshots this week: 6087
- Unique tokens from dexscreener: 798
- Unique tokens from geckoterminal: 12
- Discovery scores are exploratory, not calibrated probabilities. One 24h volume measurement is not a 4h volume measurement.
- Candidate and security statuses are NOT investment recommendations; unverified means unverified.
- 2026-11-14T20:48:40+00:00 solana SHARKBUX: needs_review, score 100.0; security not independently verified
- 2026-11-14T20:48:40+00:00 solana MEVS: needs_review, score 100.0; security not independently verified
- 2026-11-14T20:48:40+00:00 solana GATO: needs_review, score 100.0; security not independently verified
- 2026-11-14T20:48:40+00:00 solana WASTED: needs_review, score 100.0; security not independently verified
- 2026-11-14T20:48:40+00:00 solana FLAG: needs_review, score 100.0; security not independently verified
- 2026-11-14T20:48:40+00:00 solana BLOB: needs_review, score 100.0; security not independently verified
- 2026-11-14T20:48:40+00:00 solana Peekhole: needs_review, score 100.0; security not independently verified
- 2026-11-14T20:48:40+00:00 bsc 年年: needs_review, score 100.0; security not independently verified
- 2026-11-14T20:48:40+00:00 bsc TeslaSI: needs_review, score 100.0; security not independently verified
- 2026-11-14T20:48:40+00:00 bsc AGC: needs_review, score 100.0; security not independently verified
- 2026-11-14T20:48:40+00:00 solana GLITCH: needs_review, score 99.1; security not independently verified
- 2026-11-14T20:48:40+00:00 elysium VOLTA: needs_review, score 86.1; security not independently verified
- 2026-11-14T20:48:40+00:00 robinhood LOBIN: needs_review, score 71.6; security not independently verified
- 2026-11-14T20:48:40+00:00 solana Tilcayo: needs_review, score 62.3; security not independently verified
- 2026-11-14T20:48:40+00:00 robinhood FOBO: needs_review, score 62.2; security not independently verified

## V4.1 forward-only shadow evaluation (frozen rules)

- Not financial advice; no orders, no automatic weight changes.
- First observation per asset per UTC day; outcomes use same DEX pair and 1/3/7-day targets.
- Controls are a deterministic 20% sample of eligible watch-only assets, not matched random controls.
- Missing quotes and delistings are separately counted; ignoring them biases returns upward.
- 24h volume is a rolling 24h measure, not a four-hour acceleration measure.
- Frozen predictions: 1252
- signal cohort: 762 predictions
  - 1d: evaluated=695; missing=33; mean=-18.58%; positive=32.1%
  - 3d: evaluated=574; missing=101; mean=-24.25%; positive=26.0%
  - 7d: evaluated=442; missing=120; mean=-22.87%; positive=22.9%
- control cohort: 490 predictions
  - 1d: evaluated=442; missing=17; mean=-12.04%; positive=30.8%
  - 3d: evaluated=383; missing=37; mean=-5.83%; positive=26.6%
  - 7d: evaluated=279; missing=47; mean=-5.84%; positive=24.4%
- Agent B market-only support does not mean contract safety; unverified remains unverified.
- Agent A candidate / Agent B unconfirmed: 466
- Agent A watch_only / Agent B unconfirmed: 405
- Agent A candidate / Agent B supported_market_only: 295
- Agent A watch_only / Agent B supported_market_only: 85
- Agent A candidate / Agent B rejected: 1
