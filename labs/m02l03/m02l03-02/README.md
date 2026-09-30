# m02l03-02 · The target roles, as get-role describes them

**Lesson:** [Cross-Account AssumeRole Chains & Temporary STS](https://learnsome.tech/learn/cloudsecurity-course/m02l03) (lesson 2.3, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Read along

## Goal

You can design cross-account role trust that resists the confused deputy, predict when STS refuses a hop, and trace a role chain through CloudTrail.

In the lesson: These are the two roles in the production account, in the shape the get role command returns: name, A R N, maximum session duration, and the trust policy, which A W S calls the assume role policy document. The first role, prod deploy, trusts exactly one principal, the C I deployer role in the tooling account, and allows sessions of up to one hour. The second role, vendor audit, trusts the whole account of a monitoring vendor, allows sessions of up to twelve hours, and adds a condition: the caller must present one particular external I D. Keep that condition in mind; it becomes the defence against an attack you will see shortly.

## Files

- [`starter/roles.json`](starter/roles.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/roles.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–8: the first role, prod deploy
   - Lines 9–17: the second role, vendor audit

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
