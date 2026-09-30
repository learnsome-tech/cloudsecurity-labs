# m06l04-03 · Two controls, written against the real fields

**Lesson:** [Cloud Security Posture Management & Remediation](https://learnsome.tech/learn/cloudsecurity-course/m06l04) (lesson 6.4, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Read along

## Goal

You can write posture controls against real AWS Config configuration items, decide which failures to fix automatically and which to hand to a person, and build remediation with exceptions, ownership and a blast radius limit.

In the lesson: A control is a function from a configuration item to a list of problems. The first checks security groups for admin ports, S S H on twenty two and R D P on three three eight nine, open to the whole internet. It gathers the I P version four and version six ranges, keeps those with a prefix length of zero, which means every address, then tests each admin port against the rule's port range. Note the protocol minus one case. It means all traffic, and such a rule has no port range at all, which a naive check misses. The second control reads the bucket's public access block settings and reports each one that is switched off. The controls table maps a resource type to its check, and the last line loads the configuration items.

## Files

- [`starter/controls.py`](starter/controls.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/controls.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: a control is a function
   - Lines 4–13: the first checks security groups
   - Lines 14–17: the second control reads
   - Lines 18–21: the controls table
3. Notes from the lesson:
   - Line 11: Protocol -1 means all traffic and carries no port range

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l04-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
