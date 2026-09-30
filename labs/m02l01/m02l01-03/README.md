# m02l01-03 · A policy evaluator you can read on one screen

**Lesson:** [Cloud IAM Architecture & Permission Boundaries](https://learnsome.tech/learn/cloudsecurity-course/m02l01) (lesson 2.1, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Read along

## Goal

You can evaluate an AWS IAM request in the real order, spot conditions that fail open, and cap role creation with a permissions boundary.

In the lesson: Here is a small evaluator in plain Python that follows the real order, so every rule is visible. At the top, three condition operators: string equals, bool, and string like, which accepts star and question mark wildcards. The many helper exists because a policy may give one string or a list. Next, the holds function checks one condition, and notice that a key missing from the request context makes the condition false. Keep that in mind, it matters shortly. Then matches decides whether a statement applies: the action is compared ignoring case, the resource respecting case, and every condition must hold. And finally decide collects the effect of every matching statement. A deny anywhere wins, an allow comes next, and anything else falls through to implicit deny. Real I A M has more operators and policy types; this is the core that they all share.

## Files

- [`starter/iam_eval.py`](starter/iam_eval.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/iam_eval.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–2: three condition operators
   - Lines 3–5: the many helper
   - Lines 6–9: the holds function
   - Lines 10–15: matches decides whether
   - Lines 16–22: finally decide collects
3. Notes from the lesson:
   - Line 9: A key missing from the context makes the condition false
   - Line 20: Deny is checked before any allow is considered

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
