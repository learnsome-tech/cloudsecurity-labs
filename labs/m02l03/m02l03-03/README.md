# m02l03-03 · The rules STS applies to AssumeRole

**Lesson:** [Cross-Account AssumeRole Chains & Temporary STS](https://learnsome.tech/learn/cloudsecurity-course/m02l03) (lesson 2.3, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Read along

## Goal

You can design cross-account role trust that resists the confused deputy, predict when STS refuses a hop, and trace a role chain through CloudTrail.

In the lesson: This file applies the rules S T S uses for assume role, as a few lines of Python built on the evaluator from lesson one. It first loads the roles by A R N. The principals function turns a session A R N, which is what a role session calls with, into the two principals a trust policy may name: the role itself and its account root. Then assume role checks both sides in order. The caller's own identity policy must allow assume role on the target. Next, some trust statement must allow, must name one of the caller's principals, and must have its conditions hold, which is where an external I D gets checked. Because every caller here is a role session, the last check is the chaining limit of one hour. If all of that passes, it returns the new session's A R N in the target account.

## Files

- [`starter/sts_sim.py`](starter/sts_sim.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/sts_sim.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: first loads the roles
   - Lines 4–8: the principals function
   - Lines 9–12: checks both sides in order
   - Lines 13–18: some trust statement must allow
   - Lines 19–22: the chaining limit
3. Notes from the lesson:
   - Line 5: Role sessions match their role ARN and their account root
   - Line 19: Chained sessions cannot exceed one hour

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
