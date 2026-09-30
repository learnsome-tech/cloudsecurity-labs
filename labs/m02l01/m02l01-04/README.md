# m02l01-04 · The developer policy under test

**Lesson:** [Cloud IAM Architecture & Permission Boundaries](https://learnsome.tech/learn/cloudsecurity-course/m02l01) (lesson 2.1, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Read along

## Goal

You can evaluate an AWS IAM request in the real order, spot conditions that fail open, and cap role creation with a permissions boundary.

In the lesson: This is the identity policy attached to the app developer role. The first statement allows reading, writing and deleting objects in the app data bucket, and only there, because the resource is that bucket's A R N followed by a wildcard. The second statement tries to protect deletes: deny delete object whenever M F A present is false. The third one lets developers create roles whose names start with app, attach policies to them, and pass them to services. Each of these would get through a quick code review. Two of them are wrong in ways you only see by evaluating real requests, so that comes next.

## Files

- [`starter/app-dev.json`](starter/app-dev.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/app-dev.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–6: the first statement allows
   - Lines 7–9: the second statement tries
   - Lines 10–14: the third one lets developers

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l01-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
