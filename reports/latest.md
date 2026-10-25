# Weekly Social Radar Research Report
Period: 2026-10-18 to 2026-10-25 (UTC)

- Daily collection runs: 8/7 (scheduled; may be delayed or skipped)
- Candidate-day signals: 0
- Independently supported signals: 0
- Verified 1/3/7-day price outcomes: 0
- **Forecast quality: see forward-only price validation below; no skill claim without adequate samples and controls.**
- No trading. Scores are not probabilities.

## Collection limitations
- 2026-10-18: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-10-19: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-10-20: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-10-21: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-10-22: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-10-23: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-10-24: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]
- 2026-10-25: ["reddit_memecoins: HTTPError: HTTP Error 429: Too Many Requests", "reddit_cryptomoonshots: HTTPError: HTTP Error 429: Too Many Requests"]

## Source health and coverage
- coindesk: ok, 25 items
- cointelegraph: ok, 30 items
- decrypt: ok, 40 items
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

- Latest price feed: 2026-10-25 / ok / coingecko: 100 coin prices; 0 signal assets; 0 DEX contracts
- Saved price snapshots: 900
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

- dexscreener: ok, 43 runs
- geckoterminal: ok, 43 runs
- pair_collection: ok, 43 runs
- Pair snapshots this week: 6325
- Unique tokens from dexscreener: 1129
- Unique tokens from geckoterminal: 750
- Discovery scores are exploratory, not calibrated probabilities. One 24h volume measurement is not a 4h volume measurement.
- Candidate and security statuses are NOT investment recommendations; unverified means unverified.
- 2026-10-25T08:53:13+00:00 solana LARPCHECK: needs_review, score 100.0; security not independently verified
- 2026-10-25T08:53:13+00:00 solana ELON: needs_review, score 100.0; security not independently verified
- 2026-10-25T08:53:13+00:00 solana WORTHLESS: needs_review, score 100.0; security not independently verified
- 2026-10-25T08:53:13+00:00 solana BLACKTOBER: needs_review, score 100.0; security not independently verified
- 2026-10-25T08:53:13+00:00 robinhood MOTION: needs_review, score 100.0; security not independently verified
- 2026-10-25T08:53:13+00:00 ethereum DACITY: needs_review, score 100.0; security not independently verified
- 2026-10-25T08:53:13+00:00 bsc 年年: needs_review, score 100.0; security not independently verified
- 2026-10-25T08:53:13+00:00 solana ETH: needs_review, score 91.7; security not independently verified
- 2026-10-25T08:53:13+00:00 bsc CRAZYCOIN: needs_review, score 88.3; security not independently verified
- 2026-10-25T08:53:13+00:00 ethereum GROKLET: needs_review, score 87.1; security not independently verified
- 2026-10-25T08:53:13+00:00 robinhood BUSTED: needs_review, score 84.0; security not independently verified
- 2026-10-25T08:53:13+00:00 robinhood BULLISH: needs_review, score 74.2; security not independently verified
- 2026-10-25T08:53:13+00:00 robinhood OWN: needs_review, score 72.2; security not independently verified
- 2026-10-25T08:53:13+00:00 robinhood GF: needs_review, score 66.6; security not independently verified
- 2026-10-25T04:56:00+00:00 solana LARPCHECK: needs_review, score 100.0; security not independently verified

## V4.1 forward-only shadow evaluation (frozen rules)

- Not financial advice; no orders, no automatic weight changes.
- First observation per asset per UTC day; outcomes use same DEX pair and 1/3/7-day targets.
- Controls are a deterministic 20% sample of eligible watch-only assets, not matched random controls.
- Missing quotes and delistings are separately counted; ignoring them biases returns upward.
- 24h volume is a rolling 24h measure, not a four-hour acceleration measure.
- Frozen predictions: 349
- signal cohort: 231 predictions
  - 1d: evaluated=195; missing=21; mean=-30.02%; positive=25.1%
  - 3d: evaluated=106; missing=55; mean=-30.85%; positive=22.6%
  - 7d: evaluated=19; missing=7; mean=-33.77%; positive=36.8%
- control cohort: 118 predictions
  - 1d: evaluated=103; missing=6; mean=-20.77%; positive=30.1%
  - 3d: evaluated=72; missing=17; mean=+7.69%; positive=25.0%
  - 7d: evaluated=8; missing=2; mean=-39.13%; positive=25.0%
- Agent B market-only support does not mean contract safety; unverified remains unverified.
- Agent A candidate / Agent B unconfirmed: 174
- Agent A watch_only / Agent B unconfirmed: 107
- Agent A candidate / Agent B supported_market_only: 56
- Agent A watch_only / Agent B supported_market_only: 11
- Agent A candidate / Agent B rejected: 1
