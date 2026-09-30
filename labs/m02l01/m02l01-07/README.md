# m02l01-07 · An administrator role with a boundary attached

**Lesson:** [Cloud IAM Architecture & Permission Boundaries](https://learnsome.tech/learn/cloudsecurity-course/m02l01) (lesson 2.1, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Graded

## Goal

You can evaluate an AWS IAM request in the real order, spot conditions that fail open, and cap role creation with a permissions boundary.

In the lesson: The effective function takes a list of policies and applies the overlap rule: an explicit deny in any of them wins, and every one of them must say allow. Next comes the policy Priya attached, allow everything on everything, and a boundary allowing S three on the app data bucket plus CloudWatch logs. Then the same three requests are asked twice, with the admin policy alone and with the boundary added. Read the output as before and after. The app data read stays allowed. The payroll file and a backdoor user both fall to implicit deny, because the boundary never mentions them. The administrator policy is still attached; it cannot reach past the cap. For this to hold, the developer policy also needs explicit denies on deleting or rewriting the boundary, otherwise Priya removes the cap first.

## Files

- [`starter/app-dev.json`](starter/app-dev.json)
- [`starter/boundary.py`](starter/boundary.py): the listing from the lesson
- [`starter/iam_eval.py`](starter/iam_eval.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-07/starter`
2. Read `boundary.py` the way the lesson builds it:
   - Lines 1–7: the effective function takes
   - Lines 8–13: next comes the policy
   - Lines 14–21: the same three requests
3. Run it: `python3 boundary.py`.
4. Check it from the repository root: `./check m02l01-07`.

## Expected output

```text
s3:GetObject   example-app-data/reports/q3.csv allow -> allow
s3:GetObject   example-payroll/2026-09.csv    allow -> implicit deny
iam:CreateUser user/backdoor                  allow -> implicit deny
```

## How to check

`./check m02l01-07` copies `starter/` into a scratch directory and runs `python3 boundary.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
