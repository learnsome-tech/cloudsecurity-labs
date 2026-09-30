# m02l01-05 · Four requests against the developer policy

**Lesson:** [Cloud IAM Architecture & Permission Boundaries](https://learnsome.tech/learn/cloudsecurity-course/m02l01) (lesson 2.1, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Graded

## Goal

You can evaluate an AWS IAM request in the real order, spot conditions that fail open, and cap role creation with a permissions boundary.

In the lesson: The program loads the policy and builds two contexts. A console session where Priya signed in with M F A carries the key set to true. A call signed with long term access keys carries no M F A key at all, which is how A W S behaves. Then four requests, and the loop prints a verdict for each. Reading a report is allowed. Deleting the whole bucket is an implicit deny, since no statement mentions it. Now the surprise: deleting an object with an access key is allowed. The deny asked whether M F A present equals false, the key was absent, so the condition failed and the deny never applied. The fix is to flip it around: allow deletes only when M F A present is true, so an absent key fails closed. And the last line shows Priya may create a role.

## Files

- [`starter/app-dev.json`](starter/app-dev.json)
- [`starter/check_requests.py`](starter/check_requests.py): the listing from the lesson
- [`starter/iam_eval.py`](starter/iam_eval.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-05/starter`
2. Read `check_requests.py` the way the lesson builds it:
   - Lines 1–8: builds two contexts
   - Lines 9–15: then four requests
   - Lines 16–18: the loop prints
3. Notes from the lesson:
   - Line 8: Long-term access keys never send aws:MultiFactorAuthPresent
4. Run it: `python3 check_requests.py`.
5. Check it from the repository root: `./check m02l01-05`.

## Expected output

```text
s3:GetObject     example-app-data/reports/q3.csv  allow
s3:DeleteBucket  example-app-data                 implicit deny
s3:DeleteObject  example-app-data/reports/q3.csv  allow
iam:CreateRole   role/app-reporting               allow
```

## How to check

`./check m02l01-05` copies `starter/` into a scratch directory and runs `python3 check_requests.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
