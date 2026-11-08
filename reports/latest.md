# Weekly Social Radar Research Report
Period: 2026-11-01 to 2026-11-08 (UTC)

- Daily collection runs: 8/7 (scheduled; may be delayed or skipped)
- Candidate-day signals: 0
- Independently supported signals: 0
- Verified 1/3/7-day price outcomes: 0
- **Forecast quality: see forward-only price validation below; no skill claim without adequate samples and controls.**
- No trading. Scores are not probabilities.

## Collection limitations
- 2026-11-01: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-02: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-03: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-04: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-05: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-06: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-07: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-08: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]

## Source health and coverage
- coindesk: ok, 25 items
- cointelegraph: ok, 30 items
- decrypt: ok, 39 items
- google_news: ok, 46 items
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

- Latest price feed: 2026-11-08 / ok / coingecko: 100 coin prices; 0 signal assets; 0 DEX contracts
- Saved price snapshots: 2300
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

- dexscreener: ok, 42 runs
- geckoterminal: ok, 42 runs
- pair_collection: ok, 42 runs
- Pair snapshots this week: 7034
- Unique tokens from dexscreener: 1030
- Unique tokens from geckoterminal: 9
- Discovery scores are exploratory, not calibrated probabilities. One 24h volume measurement is not a 4h volume measurement.
- Candidate and security statuses are NOT investment recommendations; unverified means unverified.
- 2026-11-08T09:10:30+00:00 solana DESSA: needs_review, score 100.0; security not independently verified
- 2026-11-08T09:10:30+00:00 solana WASTED: needs_review, score 100.0; security not independently verified
- 2026-11-08T09:10:30+00:00 solana BB84: needs_review, score 100.0; security not independently verified
- 2026-11-08T09:10:30+00:00 solana nuLL: needs_review, score 100.0; security not independently verified
- 2026-11-08T09:10:30+00:00 solana VETO: needs_review, score 100.0; security not independently verified
- 2026-11-08T09:10:30+00:00 solana HEREWEGO: needs_review, score 100.0; security not independently verified
- 2026-11-08T09:10:30+00:00 solana PIRATE: needs_review, score 100.0; security not independently verified
- 2026-11-08T09:10:30+00:00 solana CATPAD: needs_review, score 100.0; security not independently verified
- 2026-11-08T09:10:30+00:00 robinhood GIGATENEV: needs_review, score 100.0; security not independently verified
- 2026-11-08T09:10:30+00:00 ethereum WASTED: needs_review, score 100.0; security not independently verified
- 2026-11-08T09:10:30+00:00 bsc GM: needs_review, score 100.0; security not independently verified
- 2026-11-08T09:10:30+00:00 bsc RM: needs_review, score 100.0; security not independently verified
- 2026-11-08T09:10:30+00:00 solana ELON: needs_review, score 99.0; security not independently verified
- 2026-11-08T09:10:30+00:00 elysium BOXA: needs_review, score 98.6; security not independently verified
- 2026-11-08T09:10:30+00:00 robinhood MOTION: needs_review, score 82.0; security not independently verified

## V4.1 forward-only shadow evaluation (frozen rules)

- Not financial advice; no orders, no automatic weight changes.
- First observation per asset per UTC day; outcomes use same DEX pair and 1/3/7-day targets.
- Controls are a deterministic 20% sample of eligible watch-only assets, not matched random controls.
- Missing quotes and delistings are separately counted; ignoring them biases returns upward.
- 24h volume is a rolling 24h measure, not a four-hour acceleration measure.
- Frozen predictions: 926
- signal cohort: 584 predictions
  - 1d: evaluated=523; missing=30; mean=-21.55%; positive=32.1%
  - 3d: evaluated=417; missing=86; mean=-19.71%; positive=28.8%
  - 7d: evaluated=298; missing=98; mean=-15.14%; positive=24.8%
- control cohort: 342 predictions
  - 1d: evaluated=312; missing=13; mean=-9.22%; positive=34.6%
  - 3d: evaluated=267; missing=30; mean=-1.49%; positive=28.8%
  - 7d: evaluated=180; missing=39; mean=-7.25%; positive=27.2%
- Agent B market-only support does not mean contract safety; unverified remains unverified.
- Agent A candidate / Agent B unconfirmed: 375
- Agent A watch_only / Agent B unconfirmed: 288
- Agent A candidate / Agent B supported_market_only: 208
- Agent A watch_only / Agent B supported_market_only: 54
- Agent A candidate / Agent B rejected: 1
