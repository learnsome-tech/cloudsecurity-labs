# m01l02-04 · Walking the tree to find misplaced accounts

**Lesson:** [AWS Organizations, Account Hierarchies & Azure Management Groups](https://learnsome.tech/learn/cloudsecurity-course/m01l02) (lesson 1.2, module 1: Multi-Account Cloud Architecture & Isolation) · Free  
**Check:** Graded

## Goal

You can lay out an AWS organisation or Azure management group tree so each account limits blast radius, and work out which accounts an organisation path condition will let in.

In the lesson: This program builds two lookup tables from that file: parent by I D, and name by I D. The ancestors function climbs from an account to the root and returns the chain root first, which is the path every policy decision follows. Then, for each account, it prints where the account sits and adds a note when the position itself is a problem. Two accounts get a note. The management account is flagged because service control policies never apply to it, so anything running there escapes every guardrail you build. Data lake prod is flagged because it sits outside every unit. A policy attached to Workloads or Prod will never reach it, even though its name says production. Both findings are about placement, not permissions, and neither would show up if you only read I A M policies.

## Files

- [`starter/org.json`](starter/org.json)
- [`starter/orgtree.py`](starter/orgtree.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-04/starter`
2. Read `orgtree.py` the way the lesson builds it:
   - Lines 1–7: two lookup tables
   - Lines 8–14: the ancestors function
   - Lines 15–21: for each account
3. Run it: `python3 orgtree.py`.
4. Check it from the repository root: `./check m01l02-04`.

## Expected output

```text
management        Root                 management account: SCPs never apply here
log-archive       Root/Security
security-tooling  Root/Security
payments-prod     Root/Workloads/Prod
payments-dev      Root/Workloads/Dev
data-lake-prod    Root                 no OU: OU policies skip it
sandbox-jo        Root/Sandbox
```

## How to check

`./check m01l02-04` copies `starter/` into a scratch directory and runs `python3 orgtree.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
