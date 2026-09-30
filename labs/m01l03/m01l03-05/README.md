# m01l03-05 · Six calls through the guardrails of payments-prod

**Lesson:** [Service Control Policies & Guardrail Architecture](https://learnsome.tech/learn/cloudsecurity-course/m01l03) (lesson 1.3, module 1: Multi-Account Cloud Architecture & Isolation) · Free  
**Check:** Graded

## Goal

You can predict whether a service control policy stack allows an API call by applying explicit deny first and then the allow-at-every-level rule, and design guardrails that enforce data residency without locking out your own platform team.

In the lesson: Here are the four levels above the payments prod account, each with Full A W S Access plus one guardrail: leaving the organisation is blocked at the root, regions at Workloads, and CloudTrail tampering at Prod. Then six calls, and the loop prints the verdict for each. Read the output line by line. Launching an instance in Ireland passes. The same launch in Oregon hits the region rule. Creating an I A M role with the requested region set to u s east one passes, because I A M is on the not action list. A developer stopping CloudTrail is denied at Prod, while platform admin gets through that rule. Platform admin cannot leave the organisation, though, because that deny names no exception. Notice that none of the three denials came from a policy attached to the account itself.

## Files

- [`starter/check.py`](starter/check.py): the listing from the lesson
- [`starter/decide.py`](starter/decide.py)
- [`starter/scp/AllowComputeAndStorage.json`](starter/scp/AllowComputeAndStorage.json)
- [`starter/scp/DenyLeaveOrg.json`](starter/scp/DenyLeaveOrg.json)
- [`starter/scp/EuRegionsOnly.json`](starter/scp/EuRegionsOnly.json)
- [`starter/scp/FullAWSAccess.json`](starter/scp/FullAWSAccess.json)
- [`starter/scp/ProtectCloudTrail.json`](starter/scp/ProtectCloudTrail.json)
- [`starter/statement.py`](starter/statement.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-05/starter`
2. Read `check.py` the way the lesson builds it:
   - Lines 1–6: four levels
   - Lines 7–12: six calls
   - Lines 13–18: prints the verdict
3. Run it: `python3 check.py`.
4. Check it from the repository root: `./check m01l03-05`.

## Expected output

```text
RunInstances      eu-west-1 developer      allowed; IAM policies decide next
RunInstances      us-west-2 developer      denied by EuRegionsOnly (Workloads)
CreateRole        us-east-1 developer      allowed; IAM policies decide next
StopLogging       eu-west-1 developer      denied by ProtectCloudTrail (Prod)
StopLogging       eu-west-1 platform-admin allowed; IAM policies decide next
LeaveOrganization us-east-1 platform-admin denied by DenyLeaveOrg (Root)
```

## How to check

`./check m01l03-05` copies `starter/` into a scratch directory and runs `python3 check.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
