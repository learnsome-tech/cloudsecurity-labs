# m02l04-02 · The reporting role, as it was first written

**Lesson:** [Least Privilege Enforcement & CIEM Architecture](https://learnsome.tech/learn/cloudsecurity-course/m02l04) (lesson 2.4, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Read along

## Goal

You can measure the gap between granted and used permissions, generate a right-sized policy from CloudTrail, and flag privilege escalation paths.

In the lesson: Here is that policy. The first statement grants every S three action on every bucket in the account, including buckets that have nothing to do with reports. The next one grants every DynamoDB action on every table, which includes deleting tables and restoring backups over them. The last statement adds all of S Q S and one K M S permission. The service itself reads a few files, queries one table, writes an export and sends one message a month. That difference is what the next programs measure.

## Files

- [`starter/reporting-role.json`](starter/reporting-role.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/reporting-role.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: every S three action
   - Lines 5–6: every DynamoDB action
   - Lines 7–9: the last statement

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
