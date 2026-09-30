# m06l01-05 · Asking the archive a question with Athena

**Lesson:** [CloudTrail Logging, Integrity Validation & Athena](https://learnsome.tech/learn/cloudsecurity-course/m06l01) (lesson 6.1, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Read along

## Goal

You can design a CloudTrail trail whose logs survive an intruder, prove with signed digests whether a log file was altered, query the archive with Athena, and write and read a Kubernetes API server audit policy.

In the lesson: Validation proves the files are genuine. Reading them is the next job, and nobody wants to search a year of compressed J S O N by hand. Athena runs S Q L directly over the files in S three, and the CloudTrail console can create the table for you. This query lists the time, the caller's A R N, the source address, the call and any error code. Two habits keep it fast and cheap. Partition the table by date, ideally with partition projection, and always filter on the partition column. Athena bills by the data it scans, so the timestamp filter turns a scan of years into a scan of one week. Then ask narrow questions, like this one: every attempt to blind the trail, whether stopping it, deleting it, updating it or changing its event selectors. Watch the error code column. An access denied here is someone testing your guardrails.

## Files

- [`starter/trail-tampering.sql`](starter/trail-tampering.sql): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/trail-tampering.sql` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–7: this query lists
   - Lines 8: the timestamp filter
   - Lines 9–12: every attempt to blind the trail

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l01-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
