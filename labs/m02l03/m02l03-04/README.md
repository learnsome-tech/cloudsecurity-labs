# m02l03-04 · Four attempts to reach production

**Lesson:** [Cross-Account AssumeRole Chains & Temporary STS](https://learnsome.tech/learn/cloudsecurity-course/m02l03) (lesson 2.3, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Graded

## Goal

You can design cross-account role trust that resists the confused deputy, predict when STS refuses a hop, and trace a role chain through CloudTrail.

In the lesson: Now some requests. The C I session is a role session in the tooling account, and its identity policy allows assume role on any production role whose name starts with prod. A dev sandbox session in the same account has that same policy. Four attempts follow. The normal deploy succeeds and returns the A R N of the new session, now living in the production account. Asking for two hours fails, because the caller is itself a role session, so this is role chaining. Asking for vendor audit fails on the caller's side, since its own policy only covers roles named prod. And the sandbox session fails on the far side: prod deploy's trust policy names only the C I deployer.

## Files

- [`starter/cross_account.py`](starter/cross_account.py): the listing from the lesson
- [`starter/iam_eval.py`](starter/iam_eval.py)
- [`starter/roles.json`](starter/roles.json)
- [`starter/sts_sim.py`](starter/sts_sim.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-04/starter`
2. Read `cross_account.py` the way the lesson builds it:
   - Lines 1–8: the C I session is a role session
   - Lines 9–15: four attempts follow
3. Run it: `python3 cross_account.py`.
4. Check it from the repository root: `./check m02l03-04`.

## Expected output

```text
ci-deployer to prod-deploy   arn:aws:sts::444455556666:assumed-role/prod-deploy/run-4812
same, for two hours          ValidationError: a chained session is limited to one hour
ci-deployer to vendor-audit  AccessDenied: the caller's own policy does not allow it
dev-sandbox to prod-deploy   AccessDenied: the role's trust policy does not match
```

## How to check

`./check m02l03-04` copies `starter/` into a scratch directory and runs `python3 cross_account.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
