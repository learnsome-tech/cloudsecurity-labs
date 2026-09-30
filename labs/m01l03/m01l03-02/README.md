# m01l03-02 · A region guardrail for data residency

**Lesson:** [Service Control Policies & Guardrail Architecture](https://learnsome.tech/learn/cloudsecurity-course/m01l03) (lesson 1.3, module 1: Multi-Account Cloud Architecture & Isolation) · Free  
**Check:** Read along

## Goal

You can predict whether a service control policy stack allows an API call by applying explicit deny first and then the allow-at-every-level rule, and design guardrails that enforce data residency without locking out your own platform team.

In the lesson: This is the most common guardrail there is: keep workloads in the regions your data residency rules allow, here Ireland and Frankfurt. It is modelled on the region deny example in the A W S documentation, with a shorter list. It is a Deny with not action, so it covers every action except the ones listed. The listed services, such as I A M, CloudFront and the global endpoint of S T S, are global. Their requests are tagged with u s east one, so denying them outside the E U would break sign in and deployments. The first condition matches when the requested region is anything other than the two allowed. The second condition carves out one role, platform admin, by A R N pattern. Both conditions must be true for the deny to apply, so the platform team can still work in other regions when it has to.

## Files

- [`starter/EuRegionsOnly.json`](starter/EuRegionsOnly.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/EuRegionsOnly.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–10: not action
   - Lines 11–15: requested region
   - Lines 16–22: the second condition

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
