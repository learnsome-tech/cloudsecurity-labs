# m01l05-02 · Three route tables and a hopeful route

**Lesson:** [Cloud Network Isolation: VPC Peering & PrivateLink](https://learnsome.tech/learn/cloudsecurity-course/m01l05) (lesson 1.5, module 1: Multi-Account Cloud Architecture & Isolation) · Free  
**Check:** Read along

## Goal

You can trace a packet through peered VPC route tables, spot CIDR overlaps that block peering, and choose between peering and PrivateLink by what each one exposes.

In the lesson: Here are three route tables in the format describe route tables returns, with the I Ds replaced by readable names. The app V P C owns ten dot one, sends ten dot two to the hub over the first peering connection, and also sends ten dot three, the data range, to that same connection, hoping the hub will pass it on. The hub owns ten dot two and has a peering connection to each side. The data V P C owns ten dot three and only knows the way back to the hub. Every table has a local route for its own range, which is how traffic inside a V P C is delivered.

## Files

- [`starter/routes.json`](starter/routes.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/routes.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: the app V P C
   - Lines 6–9: the hub owns
   - Lines 10–13: the data V P C

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
