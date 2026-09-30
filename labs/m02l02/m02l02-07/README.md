# m02l02-07 · Four tokens, one of them genuine

**Lesson:** [Workload Identity Federation: Eliminating Static Keys](https://learnsome.tech/learn/cloudsecurity-course/m02l02) (lesson 2.2, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Graded

## Goal

You can replace stored cloud keys with OIDC federation and write a trust policy that only the intended pipeline can satisfy.

In the lesson: This program mints a genuine token for the payments repository and prints what is inside it: the header with the algorithm and key id, then the five claims. Then it builds three bad tokens. The first copies the genuine token and edits the subject to name billing instead of payments, keeping the original signature. The second is correctly signed but minted for a different audience, the way a token meant for another service would look. The third expired one hundred seconds before the pinned clock. In the output, only the genuine token is accepted. The edited one fails on its signature, because changing a single byte of the payload changes what was signed. Anyone can read a J W T; nobody without the private key can alter one.

## Files

- [`starter/issuer.py`](starter/issuer.py)
- [`starter/sts.py`](starter/sts.py)
- [`starter/tokens.py`](starter/tokens.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-07/starter`
2. Read `tokens.py` the way the lesson builds it:
   - Lines 1–9: prints what is inside it
   - Lines 10–16: then it builds three bad tokens
3. Run it: `python3 tokens.py`.
4. Check it from the repository root: `./check m02l02-07`.

## Expected output

```text
{'alg': 'RS256', 'typ': 'JWT', 'kid': 'demo-key'}
  iss  https://token.actions.githubusercontent.com
  aud  sts.amazonaws.com
  sub  repo:example-org/payments-api:environment:production
  iat  1789999700
  exp  1790000000
genuine         accepted
edited sub      rejected: signature
other audience  rejected: audience
expired         rejected: expiry
```

## How to check

`./check m02l02-07` copies `starter/` into a scratch directory and runs `python3 tokens.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
