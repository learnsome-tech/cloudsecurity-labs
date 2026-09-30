# m03l03-08 · Joining the inventory to the scan results

**Lesson:** [Static Application Security Testing with Semgrep](https://learnsome.tech/learn/cloudsecurity-course/m03l03) (lesson 3.3, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Graded

## Goal

You can explain why syntax-aware SAST beats text matching, read and write a Semgrep rule for SQL built from strings, and route findings through an owned asset inventory.

In the lesson: This script joins the two halves. It loads two things: the inventory, a CSV of repository, owner, classification and status, and a folder of Semgrep JSON results, one file per repository the pipeline scanned. It walks the union of both sets of names. First, a repository with no inventory entry: it exists and gets scanned, but nobody owns its findings. Next, a decommissioned repository that still produces scan results means disposal never finished, and its pipeline and credentials are still live. Then an active repository with no scan at all, which is a coverage gap. Everything else gets its error count routed to the owner, with the classification to set priority. Read the output: the promo site has an injectable signup form and no owner, and legacy billing was retired on paper only.

## Files

- [`starter/coverage.py`](starter/coverage.py): the listing from the lesson
- [`starter/inventory.csv`](starter/inventory.csv)
- [`starter/scans/legacy-billing.json`](starter/scans/legacy-billing.json)
- [`starter/scans/payments-api.json`](starter/scans/payments-api.json)
- [`starter/scans/promo-site.json`](starter/scans/promo-site.json)
- [`starter/scans/reporting-jobs.json`](starter/scans/reporting-jobs.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-08/starter`
2. Read `coverage.py` the way the lesson builds it:
   - Lines 1–5: It loads two things
   - Lines 6–10: a repository with no inventory entry
   - Lines 11–13: a decommissioned repository
   - Lines 14–15: an active repository with no scan
   - Lines 16–19: Everything else gets
3. Run it: `python3 coverage.py`.
4. Check it from the repository root: `./check m03l03-08`.

## Expected output

```text
legacy-billing: decommissioned but still building
payments-api: 2 error(s) for team-payments, data is confidential
promo-site: scanned but not in the inventory, nobody owns it
reporting-jobs: 0 error(s) for team-data, data is confidential
web-frontend: active and never scanned, ask team-web
```

## How to check

`./check m03l03-08` copies `starter/` into a scratch directory and runs `python3 coverage.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
