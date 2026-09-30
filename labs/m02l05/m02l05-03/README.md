# m02l05-03 · The broker's decision, check by check

**Lesson:** [Zero-Trust Network Access & IdP Federation](https://learnsome.tech/learn/cloudsecurity-course/m02l05) (lesson 2.5, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Read along

## Goal

You can explain how a zero-trust broker decides each request from identity, group and device, and deprovision a user through SCIM so access ends mid-session.

In the lesson: This is the broker, a few lines of Python making the same decisions a commercial one makes. The policy names two groups and two device requirements. Beside it sit the broker's copy of the directory, kept current by S C I M, and a device inventory from device management. Decide runs for every request. First the token: verify checks the signature, the audience and the expiry, and any failure is a four oh one, sign in again. Our stand in identity provider signs with an H M A C key it shares with the broker to keep things short; real providers sign with a private key, as in lesson two. Then the directory: a disabled account is refused even with a valid token. Then the groups: at least one must grant the app. Last comes the device, where a header stands in for the client certificate, and every failed requirement is named.

## Files

- [`starter/broker.py`](starter/broker.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/broker.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–7: the policy names two groups
   - Lines 8–14: first the token
   - Lines 15–16: then the directory
   - Lines 17–18: then the groups
   - Lines 19–22: last comes the device
3. Notes from the lesson:
   - Line 19: A real broker proves the device with a certificate or its agent

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l05-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
