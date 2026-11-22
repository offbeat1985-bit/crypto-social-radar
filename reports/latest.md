# Weekly Social Radar Research Report
Period: 2026-11-15 to 2026-11-22 (UTC)

- Daily collection runs: 8/7 (scheduled; may be delayed or skipped)
- Candidate-day signals: 0
- Independently supported signals: 0
- Verified 1/3/7-day price outcomes: 0
- **Forecast quality: see forward-only price validation below; no skill claim without adequate samples and controls.**
- No trading. Scores are not probabilities.

## Collection limitations
- 2026-11-15: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-16: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-17: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-18: ["reddit_cryptocurrency: HTTPError: HTTP Error 404: Not Found", "reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-19: ["reddit_cryptocurrency: HTTPError: HTTP Error 404: Not Found", "reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-20: ["reddit_cryptocurrency: HTTPError: HTTP Error 404: Not Found", "reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-21: ["reddit_cryptocurrency: HTTPError: HTTP Error 404: Not Found", "reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-22: ["reddit_cryptocurrency: HTTPError: HTTP Error 404: Not Found", "reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]

## Source health and coverage
- coindesk: ok, 25 items
- cointelegraph: ok, 30 items
- decrypt: ok, 37 items
- google_news: ok, 49 items
- reddit_cryptocurrency: error, 0 items (HTTPError: HTTP Error 404: Not Found)
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

- Latest price feed: 2026-11-22 / ok / coingecko: 100 coin prices; 0 signal assets; 0 DEX contracts
- Saved price snapshots: 3700
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

- dexscreener: ok, 18 runs
- geckoterminal: ok, 18 runs
- pair_collection: ok, 18 runs
- Pair snapshots this week: 3031
- Unique tokens from dexscreener: 641
- Unique tokens from geckoterminal: 13
- Discovery scores are exploratory, not calibrated probabilities. One 24h volume measurement is not a 4h volume measurement.
- Candidate and security statuses are NOT investment recommendations; unverified means unverified.
- 2026-11-15T21:07:05+00:00 solana MEVS: needs_review, score 100.0; security not independently verified
- 2026-11-15T21:07:05+00:00 solana GATO: needs_review, score 100.0; security not independently verified
- 2026-11-15T21:07:05+00:00 solana Hope: needs_review, score 100.0; security not independently verified
- 2026-11-15T21:07:05+00:00 solana DacityCoin: needs_review, score 100.0; security not independently verified
- 2026-11-15T21:07:05+00:00 solana texcat: needs_review, score 100.0; security not independently verified
- 2026-11-15T21:07:05+00:00 solana Peekhole: needs_review, score 100.0; security not independently verified
- 2026-11-15T21:07:05+00:00 robinhood HSI: needs_review, score 100.0; security not independently verified
- 2026-11-15T21:07:05+00:00 bsc 年年: needs_review, score 100.0; security not independently verified
- 2026-11-15T21:07:05+00:00 solana 1WIN: needs_review, score 99.0; security not independently verified
- 2026-11-15T21:07:05+00:00 bsc TART: needs_review, score 97.4; security not independently verified
- 2026-11-15T21:07:05+00:00 bsc AGC: needs_review, score 92.5; security not independently verified
- 2026-11-15T21:07:05+00:00 solana CBUCKS: needs_review, score 91.1; security not independently verified
- 2026-11-15T21:07:05+00:00 elysium VOLTA: needs_review, score 89.3; security not independently verified
- 2026-11-15T21:07:05+00:00 solana REMUS: needs_review, score 87.2; security not independently verified
- 2026-11-15T21:07:05+00:00 robinhood BLESSED: needs_review, score 80.4; security not independently verified

## V4.1 forward-only shadow evaluation (frozen rules)

- Not financial advice; no orders, no automatic weight changes.
- First observation per asset per UTC day; outcomes use same DEX pair and 1/3/7-day targets.
- Controls are a deterministic 20% sample of eligible watch-only assets, not matched random controls.
- Missing quotes and delistings are separately counted; ignoring them biases returns upward.
- 24h volume is a rolling 24h measure, not a four-hour acceleration measure.
- Frozen predictions: 1520
- signal cohort: 890 predictions
  - 1d: evaluated=816; missing=59; mean=-19.79%; positive=30.4%
  - 3d: evaluated=682; missing=150; mean=-25.07%; positive=25.4%
  - 7d: evaluated=572; missing=190; mean=-29.56%; positive=19.8%
- control cohort: 630 predictions
  - 1d: evaluated=547; missing=52; mean=-12.01%; positive=30.2%
  - 3d: evaluated=486; missing=77; mean=-9.18%; positive=24.9%
  - 7d: evaluated=384; missing=106; mean=-11.39%; positive=21.6%
- Agent B market-only support does not mean contract safety; unverified remains unverified.
- Agent A candidate / Agent B unconfirmed: 536
- Agent A watch_only / Agent B unconfirmed: 524
- Agent A candidate / Agent B supported_market_only: 353
- Agent A watch_only / Agent B supported_market_only: 106
- Agent A candidate / Agent B rejected: 1
