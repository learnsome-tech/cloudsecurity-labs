# m02l03-07 · What an AssumeRole event records

**Lesson:** [Cross-Account AssumeRole Chains & Temporary STS](https://learnsome.tech/learn/cloudsecurity-course/m02l03) (lesson 2.3, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Read along

## Goal

You can design cross-account role trust that resists the confused deputy, predict when STS refuses a hop, and trace a role chain through CloudTrail.

In the lesson: This is the assume role event from CloudTrail, trimmed to the fields an investigator reads. The user identity is the caller: a session of the C I deployer role in the tooling account. The request parameters show which role was asked for, the session name, and the duration in seconds. The response elements hold the field that makes tracing possible, the A R N of the session just created in production. Every later call made with those credentials carries that exact A R N as its user identity. So each hop in a chain leaves a record whose output is the next hop's input.

## Files

- [`starter/assume-role-event.json`](starter/assume-role-event.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/assume-role-event.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–9: the user identity is the caller
   - Lines 10–15: the request parameters show
   - Lines 16–22: the response elements hold
3. Notes from the lesson:
   - Line 18: Later calls with these credentials carry this ARN

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
