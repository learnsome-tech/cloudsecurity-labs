# m02l02-06 · Validating a token the way STS does

**Lesson:** [Workload Identity Federation: Eliminating Static Keys](https://learnsome.tech/learn/cloudsecurity-course/m02l02) (lesson 2.2, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Read along

## Goal

You can replace stored cloud keys with OIDC federation and write a trust policy that only the intended pipeline can satisfy.

In the lesson: Now the receiving side, a few lines of Python applying the checks S T S makes. Validate splits the token into its three parts and writes the signature bytes to a file, because openssl reads signatures from files. Then openssl verifies the signature over the header and payload text, using the issuer's public key. Only after that are the claims parsed. The checks dictionary holds the four tests: the signature verified, the issuer is the registered one, the audience is S T S, and the expiry is later than now. Here, now is pinned to a fixed second so the output is identical every run. Any test that fails is named in the rejection message.

## Files

- [`starter/sts.py`](starter/sts.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/sts.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–7: validate splits the token
   - Lines 8–10: then openssl verifies
   - Lines 11–15: the checks dictionary
   - Lines 16–17: any test that fails
3. Notes from the lesson:
   - Line 5: Pinned clock for repeatable output; STS uses its own time

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
