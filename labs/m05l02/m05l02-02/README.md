# m05l02-02 · buckets.rego: two allow rules and a deny set

**Lesson:** [Policy-as-Code Architecture: OPA & Rego Syntax](https://learnsome.tech/learn/cloudsecurity-course/m05l02) (lesson 5.2, module 5: Infrastructure as Code & Policy-as-Code) · Pro  
**Check:** Read along

## Goal

You can read a Rego policy, predict its decision for a given input including undefined results, and query a decision service so that the caller fails closed.

In the lesson: Here is that rule, plus two access rules, in Rego. The package line names where the rules live, so this policy is queried as data dot platform dot buckets. Next, the default: allow is false unless something below proves otherwise. Then two rules called allow. The first says members of the platform team may do anything. The second has a body of two lines: the action is read, and the bucket's owner equals the caller's team. The deny rule is different. It uses contains, which makes deny a set of messages, and every body that matches adds one. The not keyword on the M F A line succeeds when the field is false, and also when it is missing entirely. That second case is easy to forget, and it matters for anyone writing policy.

## Files

- [`starter/buckets.rego`](starter/buckets.rego): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/buckets.rego` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: the package line names where the rules live
   - Lines 4–10: then two rules called allow
   - Lines 11–16: the deny rule is different
3. Notes from the lesson:
   - Line 3: default: the value when no allow body succeeds
   - Line 12: contains: deny is a set; each matching body adds a msg
   - Line 14: not: succeeds when mfa is false or missing

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
