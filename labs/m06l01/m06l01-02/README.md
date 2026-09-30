# m06l01-02 · One record: somebody switches the trail off

**Lesson:** [CloudTrail Logging, Integrity Validation & Athena](https://learnsome.tech/learn/cloudsecurity-course/m06l01) (lesson 6.1, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Read along

## Goal

You can design a CloudTrail trail whose logs survive an intruder, prove with signed digests whether a log file was altered, query the archive with Athena, and write and read a Kubernetes API server audit policy.

In the lesson: Here is a record in the real format, trimmed to the fields you read first. The user identity block says this was an assumed role session: the DevOps role, with the session name dev sam. The event source and event name say what happened: the CloudTrail service was asked to stop logging. The source address is where the call came from, and the user agent says it was the command line tool. Request parameters name the trail that was stopped, and read only is false, so this call changed something. Stopping the trail is the first move of a careful intruder. The stop call itself still shows up in event history and in any other trail, such as the organisation trail. The harder question is what they can do to the files already sitting in the bucket.

## Files

- [`starter/stoplogging-record.json`](starter/stoplogging-record.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/stoplogging-record.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–8: the user identity block
   - Lines 9–14: the event source and event name
   - Lines 15–22: request parameters name the trail

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l01-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
