# m01l02-03 · The organisation tree as the API describes it

**Lesson:** [AWS Organizations, Account Hierarchies & Azure Management Groups](https://learnsome.tech/learn/cloudsecurity-course/m01l02) (lesson 1.2, module 1: Multi-Account Cloud Architecture & Isolation) · Free  
**Check:** Read along

## Goal

You can lay out an AWS organisation or Azure management group tree so each account limits blast radius, and work out which accounts an organisation path condition will let in.

In the lesson: Here is that layout as data, stitched together from the list roots, list organisational units for parent and list accounts for parent calls, with the parent we asked about written onto each record. The organisation I D starts with o dash, the root with r dash, and the management account is named in the master account I D field, which is what the A P I still calls it. Next come five organisational units. Their I Ds start with ou dash and each one names its parent, so Prod and Dev sit inside Workloads. Then the accounts, each with a twelve digit I D and one parent. Look closely at data lake prod. Its parent is the root itself, which usually means somebody created it in a hurry and never moved it.

## Files

- [`starter/org.json`](starter/org.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/org.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–2: the organisation I D
   - Lines 3–8: five organisational units
   - Lines 9–19: then the accounts

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
