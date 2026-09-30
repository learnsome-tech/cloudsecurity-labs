# m06l04-02 · A configuration item for one security group

**Lesson:** [Cloud Security Posture Management & Remediation](https://learnsome.tech/learn/cloudsecurity-course/m06l04) (lesson 6.4, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Read along

## Goal

You can write posture controls against real AWS Config configuration items, decide which failures to fix automatically and which to hand to a person, and build remediation with exceptions, ownership and a blast radius limit.

In the lesson: This is what Config recorded when someone changed the bastion security group this morning. The capture time and status say when it was recorded and that the resource still exists. Resource type and resource I D are what every rule and every remediation keys on. The tags matter more than they look. Owner tells you whom to call, and managed by says Terraform controls this group, which will change how we fix it. The configuration block has the same shape the E C two describe calls return. There is one inbound permission: T C P, port twenty two, from every I P version four address on the internet.

## Files

- [`starter/sg-config-item.json`](starter/sg-config-item.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/sg-config-item.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–6: the capture time and status
   - Lines 7: the tags matter
   - Lines 8–22: the configuration block

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
