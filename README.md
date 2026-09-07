# CST Events Site — CI/CD lab

A JSON event list becomes an HTML page through a Python build script.

## Run locally (PowerShell)

```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe build_site.py
Start-Process .\dist\index.html
```

On a fresh clone, install Python, then run `python -m venv .venv` and
`.\.venv\Scripts\python.exe -m pip install pytest` first.

## What each file does

- `events.json`: source data; keep some dates in the future.
- `build_site.py`: loads events, selects today/future events, sorts, renders HTML.
- `test_build_site.py`: four deterministic tests with fixed dates.
- `.github/workflows/pipeline.yml`: test → build → deploy.
- `dist/index.html`: generated output, excluded from Git.

## Corrections to the tutorial

The boundary test must use `2027-03-01`, matching the Hackathon date.
The printed `2026-03-01` leaves two future events and fails even with correct code.
After protecting main, submit workflow changes through a pull request too;
the later instruction to push directly to main conflicts with that protection.

## GitHub setup and exercises

This workspace contains the final workflow. See [LAB_RESULTS.md](LAB_RESULTS.md)
for the actual GitHub runs demonstrating failures, repairs, and deployment gating.

1. Commit and push the initial files to `main`.
2. In Settings → Pages, choose **GitHub Actions** as the build source.
   If the initial deployment ran before this setting was enabled, rerun it.
3. In Actions, inspect the `test`, `build`, and `deploy` jobs. The build produces
   a `github-pages` artifact; deployment reports the published URL.
4. Create branch `add-event`, add a future event, commit and push, then open
   a pull request targeting main. Tests and build should pass; deploy is skipped.
5. On that branch change `>=` to `>` in `upcoming`. Push and observe the
   boundary test fail and the build/deployment skip. Restore `>=` and push.
6. Also try returning `future` without sorting. The ordering test should fail.
   Restore the sorted return and push; wait for green checks.
7. In Settings → Rules → Rulesets, create an **Active** branch ruleset targeting
   `main`. Require a pull request and required checks `test` and `build`.
   Require zero approving reviews for this solo lab. Avoid a bypass for yourself
   if you want to demonstrate a refused direct push. Do not require `deploy`:
   it intentionally skips on pull requests. Do not enable “Restrict updates”:
   requiring a pull request is the rule that blocks direct pushes while allowing merges.
8. Verify that a trivial direct commit on main is refused. Preserve that commit
   on another branch before bringing local main back in sync; do not force-push.
9. Merge the green event pull request. Watch all three jobs pass on main and
   confirm the new event appears on the live site.

Record actual run links for each failure and repair; local test results are not
evidence that GitHub checks, branch protection, or deployment have run.

Reference: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
