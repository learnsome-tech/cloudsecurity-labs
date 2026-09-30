# m02l04-05 · Generating a policy from what was actually used

**Lesson:** [Least Privilege Enforcement & CIEM Architecture](https://learnsome.tech/learn/cloudsecurity-course/m02l04) (lesson 2.4, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Graded

## Goal

You can measure the gap between granted and used permissions, generate a right-sized policy from CloudTrail, and flag privilege escalation paths.

In the lesson: Now build the replacement. The program groups the observed actions by the scope they touched, then builds one allow statement per scope. I A M Access Analyzer can generate a starting policy from CloudTrail in a similar spirit. The generated policy has six statements: read items from the orders table, decrypt with one key, list the reports bucket, write under exports, read under monthly, and send to one queue. Then three test requests go through the evaluator from lesson one. Next month's report is allowed, because the folder was widened. The payroll bucket and deleting the reports bucket are both implicit denies now. Before you swap it in, run the new policy beside the old one and watch for access denied errors.

## Files

- [`starter/iam_eval.py`](starter/iam_eval.py)
- [`starter/rightsize.py`](starter/rightsize.py): the listing from the lesson
- [`starter/trail-90d.json`](starter/trail-90d.json)
- [`starter/trail.py`](starter/trail.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-05/starter`
2. Read `rightsize.py` the way the lesson builds it:
   - Lines 1–7: groups the observed actions
   - Lines 8–12: builds one allow statement
   - Lines 13–19: three test requests
3. Run it: `python3 rightsize.py`.
4. Check it from the repository root: `./check m02l04-05`.

## Expected output

```text
dynamodb:GetItem, dynamodb:Query on table/orders
kms:Decrypt on key/1234abcd-12ab-34cd-56ef-1234567890ab
s3:ListBucket on example-reports
s3:PutObject on example-reports/exports/*
s3:GetObject on example-reports/monthly/*
sqs:SendMessage on report-ready
s3:GetObject     example-reports/monthly/2026-10.csv  allow
s3:GetObject     example-payroll/2026-09.csv          implicit deny
s3:DeleteBucket  example-reports                      implicit deny
```

## How to check

`./check m02l04-05` copies `starter/` into a scratch directory and runs `python3 rightsize.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
