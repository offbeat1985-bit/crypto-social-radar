# Crypto Social Radar – Android-friendly upload edition

Free research prototype. No trades, paid services, exchange keys, or wallet access.

## Upload mapping

| Downloaded file | GitHub repository path | How |
|---|---|---|
| `radar.py` | `radar.py` | Upload file in repository root |
| `README.md` | `README.md` | Upload file in repository root (replace initial README if needed) |
| `daily.yml` | `.github/workflows/daily.yml` | GitHub **Add file > Create new file**; type the complete path in the filename field, paste the content of downloaded `daily.yml` |
| `weekly.yml` | `.github/workflows/weekly.yml` | Same procedure with `weekly.yml` |

Do not upload the YAML files to the root: GitHub Actions only discovers workflow files inside `.github/workflows/`.

## Enable

1. Repository must have **Actions** and **Issues** enabled.
2. Settings > Actions > General > Workflow permissions > **Read and write permissions**.
3. Actions > Daily collection and two-agent analysis > Run workflow.
4. Actions > Weekly research report > Run workflow.
5. `data/radar.sqlite3` and `reports/latest.md` are generated automatically. Do not upload database, caches or sample reports.

## Limits

- The two agents are separate rule-based modules, **not independent LLMs**.
- RSS data access can fail and does not cover all coins.
- **No actual forecast quality metric yet**: price outcomes and baselines are not implemented.
- GitHub Actions schedules are best-effort; verify run logs.
- The Sunday issue is a weekly research summary; no guarantee of email or push delivery.
- Keep the repository private if you do not want the research history public.
