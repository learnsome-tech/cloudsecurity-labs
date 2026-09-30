# m02l03-08 · Walking a chain back to its origin

**Lesson:** [Cross-Account AssumeRole Chains & Temporary STS](https://learnsome.tech/learn/cloudsecurity-course/m02l03) (lesson 2.3, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Graded

## Goal

You can design cross-account role trust that resists the confused deputy, predict when STS refuses a hop, and trace a role chain through CloudTrail.

In the lesson: That link is all you need to walk a chain backwards. The program loads a trail file with events from both accounts, the way an organisation trail collects them, and indexes every assume role event by the session A R N it issued. It then picks the suspicious production call, a put bucket policy, and prints who made it. The loop looks up the event that created that session, prints it, and moves on to its caller, repeating until the caller is not a role session. The output reads from the change back to its origin: the prod deploy session, created by the C I deployer session, created from a GitHub token whose subject is the payments repository's production environment. The read only session belonging to Alice is in the same file, and the trace correctly ignores it.

## Files

- [`starter/trace_chain.py`](starter/trace_chain.py): the listing from the lesson
- [`starter/trail.json`](starter/trail.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-08/starter`
2. Read `trace_chain.py` the way the lesson builds it:
   - Lines 1–5: indexes every assume role event
   - Lines 6–9: picks the suspicious production call
   - Lines 10–14: the loop looks up
3. Run it: `python3 trace_chain.py`.
4. Check it from the repository root: `./check m02l03-08`.

## Expected output

```text
2026-09-14T09:13:40Z PutBucketPolicy by arn:aws:sts::444455556666:assumed-role/prod-deploy/run-4812
2026-09-14T09:12:04Z AssumeRole from arn:aws:sts::111122223333:assumed-role/ci-deployer/run-4812
2026-09-14T09:12:01Z AssumeRoleWithWebIdentity from WebIdentityUser repo:example-org/payments-api:environment:production
```

## How to check

`./check m02l03-08` copies `starter/` into a scratch directory and runs `python3 trace_chain.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
