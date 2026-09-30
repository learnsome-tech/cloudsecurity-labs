# m02l04-03 · Turning CloudTrail events into permissions

**Lesson:** [Least Privilege Enforcement & CIEM Architecture](https://learnsome.tech/learn/cloudsecurity-course/m02l04) (lesson 2.4, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Read along

## Goal

You can measure the gap between granted and used permissions, generate a right-sized policy from CloudTrail, and flag privilege escalation paths.

In the lesson: To compare granted with used, each logged event has to become the permission it needed. That starts with a small alias table, because a few A P I names differ from the I A M action they need: list objects version two is authorised by list bucket, and head object by get object. Next, action of builds the service prefix from the event source and joins it to the event name. Then scope of picks the resource. For S three objects it widens the key to its folder, so a new monthly file tomorrow is still covered. Finally, calls reads a trail file and returns the action and scope of every event made by one role, recognised by the role name inside its session A R N.

## Files

- [`starter/trail.py`](starter/trail.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/trail.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: a small alias table
   - Lines 4–7: action of builds
   - Lines 8–13: scope of picks the resource
   - Lines 14–18: calls reads a trail file
3. Notes from the lesson:
   - Line 3: A few API names differ from the IAM action they need

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l04-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
