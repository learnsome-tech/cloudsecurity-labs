# m01l04-06 · A domain allow list rule group

**Lesson:** [Security Landing Zones & Centralized Egress Inspection](https://learnsome.tech/learn/cloudsecurity-course/m01l04) (lesson 1.4, module 1: Multi-Account Cloud Architecture & Isolation) · Free  
**Check:** Read along

## Goal

You can describe the baseline a security landing zone gives every new account, review Kubernetes control plane and kubelet flags against CIS benchmark expectations, and explain what a centralised domain allow list really inspects and how it can be bypassed.

In the lesson: This is the input for creating a stateful rule group in A W S Network Firewall. The capacity is fixed when the group is created, so leave room to grow. The rule variables set home net to the whole ten dot range, which covers every spoke. Then the targets. A name with a leading dot, such as dot example dot com, matches that domain and every subdomain. A name without one, such as pypi dot org, matches only itself. The target types say where the name is read from: the T L S server name indication for encrypted traffic, and the H T T P host header for plain web traffic. Allow list generates rules that pass those names and drop any other T L S or H T T P traffic. Traffic that is neither, such as SSH, needs rules of its own.

## Files

- [`starter/egress-domain-allowlist.json`](starter/egress-domain-allowlist.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/egress-domain-allowlist.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: a stateful rule group
   - Lines 5–10: home net
   - Lines 11–19: the targets

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l04-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
