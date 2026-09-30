# m02l03-06 · The confused deputy, with and without the condition

**Lesson:** [Cross-Account AssumeRole Chains & Temporary STS](https://learnsome.tech/learn/cloudsecurity-course/m02l03) (lesson 2.3, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Graded

## Goal

You can design cross-account role trust that resists the confused deputy, predict when STS refuses a hop, and trace a role chain through CloudTrail.

In the lesson: Here is that scenario, reusing the same assume role rules. The scanner is a role session in the vendor's account, allowed to assume any role at all. The vendor's tenant table holds two customers. Both point at the victim's role, because the attacker typed its A R N, but each carries the external I D the vendor assigned to that tenant. The run jobs function assumes every tenant's role, sending that tenant's external I D. It runs first with the trust policy as written: the owner's job succeeds and the attacker's is refused. Then the program deletes the condition, which is what many first attempts at vendor access look like, and runs the jobs again. This time the attacker's job receives a session in the victim's account.

## Files

- [`starter/iam_eval.py`](starter/iam_eval.py)
- [`starter/roles.json`](starter/roles.json)
- [`starter/sts_sim.py`](starter/sts_sim.py)
- [`starter/vendor.py`](starter/vendor.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-06/starter`
2. Read `vendor.py` the way the lesson builds it:
   - Lines 1–5: the scanner is a role session
   - Lines 6–8: the vendor's tenant table
   - Lines 9–14: the run jobs function
   - Lines 15–20: first with the trust policy as written
3. Run it: `python3 vendor.py`.
4. Check it from the repository root: `./check m02l03-06`.

## Expected output

```text
trust policy requires the ExternalId:
  customer-4471, the owner  arn:aws:sts::444455556666:assumed-role/vendor-audit/scan
  customer-9020, attacker   AccessDenied: the role's trust policy does not match
trust policy without the condition:
  customer-4471, the owner  arn:aws:sts::444455556666:assumed-role/vendor-audit/scan
  customer-9020, attacker   arn:aws:sts::444455556666:assumed-role/vendor-audit/scan
```

## How to check

`./check m02l03-06` copies `starter/` into a scratch directory and runs `python3 vendor.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
