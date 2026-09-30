# m06l02-06 · An EventBridge rule for high severity findings

**Lesson:** [Threat Detection with GuardDuty & Anomaly Analytics](https://learnsome.tech/learn/cloudsecurity-course/m06l02) (lesson 6.2, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Read along

## Goal

You can read a GuardDuty finding, reproduce the evidence behind it from CloudTrail, explain what an anomaly baseline flags and misses, and route findings with an EventBridge pattern that does not drop the quiet ones.

In the lesson: Findings reach the rest of your tooling through EventBridge. Every finding arrives as an event whose source is aws dot guardduty and whose detail type is GuardDuty Finding. New findings are sent within minutes, and updates to existing ones on a schedule you choose. An event pattern selects the ones you care about. Two rules explain almost every pattern. Separate fields must all match, so this is an and. Values inside one list are alternatives, so that is an or. The detail block adds a numeric comparison: severity seven or more. The rule's target might be a paging service, a chat channel, or a function that isolates the instance. This is the pattern most teams write first.

## Files

- [`starter/high-severity.json`](starter/high-severity.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/high-severity.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: every finding arrives
   - Lines 4–7: the detail block

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l02-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
