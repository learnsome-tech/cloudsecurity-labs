# m02l05-04 · A real HTTP server with a SCIM endpoint

**Lesson:** [Zero-Trust Network Access & IdP Federation](https://learnsome.tech/learn/cloudsecurity-course/m02l05) (lesson 2.5, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Read along

## Goal

You can explain how a zero-trust broker decides each request from identity, group and device, and deprovision a user through SCIM so access ends mid-session.

In the lesson: The server wraps that decision in an H T T P server from the standard library. Reply sends a status code and a short text. Do get runs decide for every request to the app, with the clock pinned so the output repeats. Do patch is the S C I M endpoint. It reads the user's S C I M I D from the path, finds that user, parses the patch operations from the body, and applies any replace on the active attribute. That is the message an identity provider sends when someone is offboarded. A real endpoint would also demand the identity provider's bearer token; this one skips it to stay short, and you will add it in the exercise.

## Files

- [`starter/server.py`](starter/server.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/server.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–9: reply sends a status
   - Lines 10–12: do get runs decide
   - Lines 13–21: do patch is the S C I M endpoint

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l05-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
