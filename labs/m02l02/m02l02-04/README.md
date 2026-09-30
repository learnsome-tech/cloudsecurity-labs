# m02l02-04 · The AWS side: a trust policy that pins the subject

**Lesson:** [Workload Identity Federation: Eliminating Static Keys](https://learnsome.tech/learn/cloudsecurity-course/m02l02) (lesson 2.2, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Read along

## Goal

You can replace stored cloud keys with OIDC federation and write a trust policy that only the intended pipeline can satisfy.

In the lesson: This trust policy sits on the payments deploy role. The action is assume role with web identity, the federated call. The principal is the O I D C provider you registered once in the account for GitHub's issuer. Then come two conditions. The audience must be S T S, so a token minted for some other service is useless here. And the subject must equal one exact string: the payments A P I repository, running in the production environment. That string names both the repository and the part of its workflow the call comes from. Everything else a token might say is ignored unless you add a condition for it.

## Files

- [`starter/trust-policy.json`](starter/trust-policy.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/trust-policy.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: the action is assume role
   - Lines 6–9: the principal is the O I D C provider
   - Lines 10–16: then come two conditions
   - Lines 17–18: everything else a token might say

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
