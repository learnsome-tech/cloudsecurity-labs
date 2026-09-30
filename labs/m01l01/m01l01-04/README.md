# m01l01-04 · A security group export in the real API format

**Lesson:** [Shared Responsibility Model & Cloud Threat Landscapes](https://learnsome.tech/learn/cloudsecurity-course/m01l01) (lesson 1.1, module 1: Multi-Account Cloud Architecture & Isolation) · Free  
**Check:** Read along

## Goal

You can say which security tasks stay with you in each cloud service model, audit a real security group export for admin ports open to the internet, and check bucket regions against a data residency rule.

In the lesson: Most customer side threats come from settings like these. This is the shape of output from the A W S command describe security groups, trimmed to five groups. Each group has a list of I P permissions. A rule names a protocol, a port range and the address ranges allowed in, with I P version four and I P version six ranges kept in separate lists. Web allows port four hundred and forty three from anywhere, which is what a public site needs. Now look at the legacy admin group: protocol minus one means every protocol and every port, and its source is the entire I P version six internet. Now look at ops tools. Nobody typed zero zero zero zero slash zero, yet slash one still covers half of every I P version four address there is.

## Files

- [`starter/sg.json`](starter/sg.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/sg.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: each group has a list
   - Lines 6–17: look at the legacy admin group
   - Lines 18–22: now look at ops tools

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l01-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
