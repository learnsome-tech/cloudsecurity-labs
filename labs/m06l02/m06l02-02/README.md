# m06l02-02 · Anatomy of a finding

**Lesson:** [Threat Detection with GuardDuty & Anomaly Analytics](https://learnsome.tech/learn/cloudsecurity-course/m06l02) (lesson 6.2, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Read along

## Goal

You can read a GuardDuty finding, reproduce the evidence behind it from CloudTrail, explain what an anomaly baseline flags and misses, and route findings with an EventBridge pattern that does not drop the quiet ones.

In the lesson: The type string is the headline, and it has a grammar. Before the colon, the threat purpose: unauthorised access. Then the kind of resource affected, then the threat family, instance credential exfiltration, and after the dot, how it was detected: outside A W S. Severity is a number, and seven or more means high or critical. The resource block says whose keys these are: a temporary access key for the app server role, and the principal I D ends in an instance I D. So these are credentials that the instance metadata service handed to one E C two instance. The action block says what was done with them: list buckets, from an address that is not that instance. Count says the activity has repeated three times; repeats update this finding instead of creating new ones.

## Files

- [`starter/finding.json`](starter/finding.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/finding.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: the type string is the headline
   - Lines 6–14: the resource block
   - Lines 15–22: the action block

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
