# m02l04-04 · Measuring the gap between granted and used

**Lesson:** [Least Privilege Enforcement & CIEM Architecture](https://learnsome.tech/learn/cloudsecurity-course/m02l04) (lesson 2.4, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Graded

## Goal

You can measure the gap between granted and used permissions, generate a right-sized policy from CloudTrail, and flag privilege escalation paths.

In the lesson: This program loads the policy, a list of real action names for these four services, and ninety days of trail cut down to one event per distinct call. It expands the policy's wildcards against that action list to get everything granted, and collects everything used. The first line is the headline: dozens granted, a handful used. Then for each service it counts the unused actions and names the ones that destroy data or change who can reach it. Deleting tables and buckets, purging queues, rewriting bucket policies: none of them has been called once, yet any attacker holding this role's credentials could call them all. That list is what you bring to the service owner.

## Files

- [`starter/actions.json`](starter/actions.json)
- [`starter/iam_eval.py`](starter/iam_eval.py)
- [`starter/reporting-role.json`](starter/reporting-role.json)
- [`starter/trail-90d.json`](starter/trail-90d.json)
- [`starter/trail.py`](starter/trail.py)
- [`starter/unused.py`](starter/unused.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-04/starter`
2. Read `unused.py` the way the lesson builds it:
   - Lines 1–10: expands the policy's wildcards
   - Lines 11–18: for each service
3. Run it: `python3 unused.py`.
4. Check it from the repository root: `./check m02l04-04`.

## Expected output

```text
granted 32, used 7, unused 25
dynamodb 10 unused; destructive: DeleteItem DeleteTable
kms       0 unused; destructive:
s3       10 unused; destructive: DeleteBucket DeleteBucketPolicy DeleteObject PutBucketAcl PutBucketPolicy PutBucketPublicAccessBlock
sqs       5 unused; destructive: DeleteMessage DeleteQueue PurgeQueue
```

## How to check

`./check m02l04-04` copies `starter/` into a scratch directory and runs `python3 unused.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
