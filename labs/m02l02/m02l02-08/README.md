# m02l02-08 · Why the subject condition is the real defence

**Lesson:** [Workload Identity Federation: Eliminating Static Keys](https://learnsome.tech/learn/cloudsecurity-course/m02l02) (lesson 2.2, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Graded

## Goal

You can replace stored cloud keys with OIDC federation and write a trust policy that only the intended pipeline can satisfy.

In the lesson: A valid signature proves GitHub issued the token, and GitHub will issue one to any repository on the platform, an attacker's included. So the trust policy has to do the rest. This program reuses the holds function from lesson one and turns the claims into condition keys prefixed with the provider's host name, which is how I A M names them. It compares three trust policies: the exact one from our file, an organisation wildcard, and one that checks only the audience. Then four subjects are tested. The exact policy accepts only the production deploy. The wildcard also lets in pull requests and a sandbox repository that anyone in the organisation can push to. The audience only policy accepts a stranger's repository, which means anybody on GitHub could deploy into your account.

## Files

- [`starter/iam_eval.py`](starter/iam_eval.py)
- [`starter/trust-policy.json`](starter/trust-policy.json)
- [`starter/trust_check.py`](starter/trust_check.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-08/starter`
2. Read `trust_check.py` the way the lesson builds it:
   - Lines 1–8: reuses the holds function
   - Lines 9–15: compares three trust policies
   - Lines 16–22: four subjects are tested
3. Run it: `python3 trust_check.py`.
4. Check it from the repository root: `./check m02l02-08`.

## Expected output

```text
subject                                              exact org   aud-only
repo:example-org/payments-api:environment:production True  True  True
repo:example-org/payments-api:pull_request           False True  True
repo:example-org/sandbox:ref:refs/heads/main         False True  True
repo:someone-else/tools:ref:refs/heads/main          False False True
```

## How to check

`./check m02l02-08` copies `starter/` into a scratch directory and runs `python3 trust_check.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
