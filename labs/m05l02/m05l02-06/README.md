# m05l02-06 · buckets_test.rego: policy gets unit tests

**Lesson:** [Policy-as-Code Architecture: OPA & Rego Syntax](https://learnsome.tech/learn/cloudsecurity-course/m05l02) (lesson 5.2, module 5: Infrastructure as Code & Policy-as-Code) · Pro  
**Check:** Read along

## Goal

You can read a Rego policy, predict its decision for a given input including undefined results, and query a decision service so that the caller fails closed.

In the lesson: Policy is code, so it gets unit tests, and OPA runs them itself. A test is a rule whose name starts with test, and it passes when its body succeeds. The with keyword replaces the input for one expression, so each test builds exactly the request it cares about. The first test proves an owner can read their own team's bucket. The second proves a delete without M F A produces exactly one deny message. Running opa test on the folder evaluates every test rule and reports passes and failures with a count. Put that command in the policy repository's pipeline, so a change to Rego is reviewed and tested the way a change to Go would be. A third test for a stranger's request, expecting allow to be false, would catch anyone deleting the default line.

## Files

- [`starter/buckets_test.rego`](starter/buckets_test.rego): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/buckets_test.rego` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: a test is a rule whose name starts with test
   - Lines 5–12: the first test proves an owner can read
   - Lines 13–19: the second proves a delete without M F A

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l02-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
