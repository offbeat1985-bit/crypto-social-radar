# Weekly Social Radar Research Report
Period: 2026-10-25 to 2026-11-01 (UTC)

- Daily collection runs: 8/7 (scheduled; may be delayed or skipped)
- Candidate-day signals: 0
- Independently supported signals: 0
- Verified 1/3/7-day price outcomes: 0
- **Forecast quality: see forward-only price validation below; no skill claim without adequate samples and controls.**
- No trading. Scores are not probabilities.

## Collection limitations
- 2026-10-25: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-10-26: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-10-27: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-10-28: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-10-29: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-10-30: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-10-31: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-11-01: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]

## Source health and coverage
- coindesk: ok, 25 items
- cointelegraph: ok, 30 items
- decrypt: ok, 39 items
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

- Latest price feed: 2026-11-01 / ok / coingecko: 100 coin prices; 0 signal assets; 0 DEX contracts
- Saved price snapshots: 1600
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
- Pair snapshots this week: 6107
- Unique tokens from dexscreener: 950
- Unique tokens from geckoterminal: 9
- Discovery scores are exploratory, not calibrated probabilities. One 24h volume measurement is not a 4h volume measurement.
- Candidate and security statuses are NOT investment recommendations; unverified means unverified.
- 2026-11-01T09:06:03+00:00 solana ANTS: needs_review, score 100.0; security not independently verified
- 2026-11-01T09:06:03+00:00 solana LARPCHECK: needs_review, score 100.0; security not independently verified
- 2026-11-01T09:06:03+00:00 solana Bitcoin: needs_review, score 100.0; security not independently verified
- 2026-11-01T09:06:03+00:00 solana jeff: needs_review, score 100.0; security not independently verified
- 2026-11-01T09:06:03+00:00 solana WASTED: needs_review, score 100.0; security not independently verified
- 2026-11-01T09:06:03+00:00 solana Leverhedge: needs_review, score 100.0; security not independently verified
- 2026-11-01T09:06:03+00:00 solana CHOO: needs_review, score 100.0; security not independently verified
- 2026-11-01T09:06:03+00:00 solana DacityCoin: needs_review, score 100.0; security not independently verified
- 2026-11-01T09:06:03+00:00 solana NETWORK: needs_review, score 100.0; security not independently verified
- 2026-11-01T09:06:03+00:00 solana BLOB: needs_review, score 100.0; security not independently verified
- 2026-11-01T09:06:03+00:00 solana tipr: needs_review, score 100.0; security not independently verified
- 2026-11-01T09:06:03+00:00 solana CATPAD: needs_review, score 100.0; security not independently verified
- 2026-11-01T09:06:03+00:00 robinhood LOBIN: needs_review, score 100.0; security not independently verified
- 2026-11-01T09:06:03+00:00 robinhood DODO: needs_review, score 100.0; security not independently verified
- 2026-11-01T09:06:03+00:00 bsc 年年: needs_review, score 100.0; security not independently verified

## V4.1 forward-only shadow evaluation (frozen rules)

- Not financial advice; no orders, no automatic weight changes.
- First observation per asset per UTC day; outcomes use same DEX pair and 1/3/7-day targets.
- Controls are a deterministic 20% sample of eligible watch-only assets, not matched random controls.
- Missing quotes and delistings are separately counted; ignoring them biases returns upward.
- 24h volume is a rolling 24h measure, not a four-hour acceleration measure.
- Frozen predictions: 624
- signal cohort: 403 predictions
  - 1d: evaluated=330; missing=26; mean=-25.67%; positive=30.6%
  - 3d: evaluated=227; missing=68; mean=-27.68%; positive=25.1%
  - 7d: evaluated=156; missing=74; mean=-34.39%; positive=22.4%
- control cohort: 221 predictions
  - 1d: evaluated=191; missing=8; mean=-14.08%; positive=34.0%
  - 3d: evaluated=142; missing=22; mean=+2.91%; positive=26.1%
  - 7d: evaluated=92; missing=26; mean=-21.17%; positive=27.2%
- Agent B market-only support does not mean contract safety; unverified remains unverified.
- Agent A candidate / Agent B unconfirmed: 277
- Agent A watch_only / Agent B unconfirmed: 194
- Agent A candidate / Agent B supported_market_only: 125
- Agent A watch_only / Agent B supported_market_only: 27
- Agent A candidate / Agent B rejected: 1
