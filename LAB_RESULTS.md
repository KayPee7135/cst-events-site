# CI/CD lab evidence

Executed on 7 September 2026 in `KayPee7135/cst-events-site`.

## Verified runs

| Exercise | Evidence | Result |
| --- | --- | --- |
| Initial test, build and Pages deployment | [Run 34139613315](https://github.com/KayPee7135/cst-events-site/actions/runs/34139613315) | All three jobs passed |
| Change `>=` to `>` | [Run 34139714492](https://github.com/KayPee7135/cst-events-site/actions/runs/34139714492) | Boundary test failed; build and deploy skipped |
| Restore `>=` | [Run 34139806479](https://github.com/KayPee7135/cst-events-site/actions/runs/34139806479) | Pipeline passed |
| Add an event through a PR | [Run 34139858890](https://github.com/KayPee7135/cst-events-site/actions/runs/34139858890) | Test/build passed; deploy skipped |
| Remove sorting on that PR | [Run 34139956453](https://github.com/KayPee7135/cst-events-site/actions/runs/34139956453) | Ordering test failed; build/deploy skipped; PR merge state BLOCKED |

The [event pull request](https://github.com/KayPee7135/cst-events-site/pull/1)
preserves the passing, deliberately failing, and repaired revisions.

## Main protection

[Active ruleset](https://github.com/KayPee7135/cst-events-site/rules/22463533)
requires a pull request, the GitHub Actions `test` and `build` checks, and an
up-to-date branch. Approving review count is zero for this solo repository.
Force pushes and branch deletion are blocked. There are no bypass actors.

An empty demonstration commit was preserved locally on `codex/protection-proof`.
Pushing it directly to main was rejected by GitHub:

```text
GH013: Repository rule violations found for refs/heads/main.
Changes must be made through a pull request.
2 of 2 required status checks are expected.
push declined due to repository rule violations
```

## Deployment gate

Before merging, the live site was fetched and contained exactly the original
three upcoming events. The unmerged GitHub Actions Workshop was absent.
The PR's successful run explicitly reported `deploy: skipped`.

After merging a passing PR, its main-branch run publishes automatically.
See the [Actions history](https://github.com/KayPee7135/cst-events-site/actions)
and [live site](https://kaypee7135.github.io/cst-events-site/).

## Tutorial corrections and scope

- Fixed the boundary test's date from `2026-03-01` to `2027-03-01` to match
  the fixture; otherwise the supplied test fails even with correct code.
- Workflow edits after protecting main must also use a pull request.
- The final workflow was installed directly; the intermediate test-only
  workflow and generic `site` artifact were not separate historical runs.
  The real builds use the deployable `github-pages` artifact.
