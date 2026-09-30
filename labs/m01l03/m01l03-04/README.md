# m01l03-04 · Deny anywhere wins; allow must appear at every level

**Lesson:** [Service Control Policies & Guardrail Architecture](https://learnsome.tech/learn/cloudsecurity-course/m01l03) (lesson 1.3, module 1: Multi-Account Cloud Architecture & Isolation) · Free  
**Check:** Read along

## Goal

You can predict whether a service control policy stack allows an API call by applying explicit deny first and then the allow-at-every-level rule, and design guardrails that enforce data residency without locking out your own platform team.

In the lesson: Now the rule for a whole organisation path. The levels are the root, each unit on the way down, and the account itself, and load reads policies from disk for each one. The first pass looks at every statement at every level. One matching deny anywhere ends the decision, and no allow can override it. The second pass is the one people forget. At each level, at least one attached policy must allow the call. It is an intersection, not a union. An allow on the account does nothing if the unit above it allows less. If a call survives both passes, the service control policies are out of the way, and the account's own I A M policies decide what happens next.

## Files

- [`starter/decide.py`](starter/decide.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/decide.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–8: load reads policies
   - Lines 9–14: first pass
   - Lines 15–19: the second pass

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l03-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
