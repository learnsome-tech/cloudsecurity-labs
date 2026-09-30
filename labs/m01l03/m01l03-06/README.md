# m01l03-06 · One narrow allow list above the account

**Lesson:** [Service Control Policies & Guardrail Architecture](https://learnsome.tech/learn/cloudsecurity-course/m01l03) (lesson 1.3, module 1: Multi-Account Cloud Architecture & Isolation) · Free  
**Check:** Graded

## Goal

You can predict whether a service control policy stack allows an API call by applying explicit deny first and then the allow-at-every-level rule, and design guardrails that enforce data residency without locking out your own platform team.

In the lesson: Now the classic outage. Somebody swapped Full A W S Access on the Workloads unit for an allow list that names only E C two and S three, reasoning that the account below still has Full A W S Access. We try five calls an ordinary application makes. Only the first two survive. Decrypting with K M S, writing logs and assuming a role all fail at Workloads, because nothing at that level allows them, and the allow on the account cannot reach past it. In a real account, that shows up as access denied errors in every application at once, including reads of encrypted S three objects. Allow lists are a legitimate strategy, but they need every service the platform uses, and they are best tested against a sandbox unit first.

## Files

- [`starter/decide.py`](starter/decide.py)
- [`starter/narrow.py`](starter/narrow.py): the listing from the lesson
- [`starter/scp/AllowComputeAndStorage.json`](starter/scp/AllowComputeAndStorage.json)
- [`starter/scp/DenyLeaveOrg.json`](starter/scp/DenyLeaveOrg.json)
- [`starter/scp/EuRegionsOnly.json`](starter/scp/EuRegionsOnly.json)
- [`starter/scp/FullAWSAccess.json`](starter/scp/FullAWSAccess.json)
- [`starter/scp/ProtectCloudTrail.json`](starter/scp/ProtectCloudTrail.json)
- [`starter/statement.py`](starter/statement.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-06/starter`
2. Read `narrow.py` the way the lesson builds it:
   - Lines 1–7: swapped full a w s access
   - Lines 8–13: five calls
3. Run it: `python3 narrow.py`.
4. Check it from the repository root: `./check m01l03-06`.

## Expected output

```text
ec2:RunInstances   allowed; IAM policies decide next
s3:GetObject       allowed; IAM policies decide next
kms:Decrypt        no Allow at Workloads
logs:PutLogEvents  no Allow at Workloads
sts:AssumeRole     no Allow at Workloads
```

## How to check

`./check m01l03-06` copies `starter/` into a scratch directory and runs `python3 narrow.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
