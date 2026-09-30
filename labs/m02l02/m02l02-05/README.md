# m02l02-05 · A stand-in issuer that signs tokens like GitHub

**Lesson:** [Workload Identity Federation: Eliminating Static Keys](https://learnsome.tech/learn/cloudsecurity-course/m02l02) (lesson 2.2, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Read along

## Goal

You can replace stored cloud keys with OIDC federation and write a trust policy that only the intended pipeline can satisfy.

In the lesson: To watch those checks happen we need tokens, and GitHub only mints them inside a workflow. So this file plays the issuer with a throwaway key pair. At the top, openssl generates an R S A private key and writes out the public half, which is the part a real issuer publishes for anyone to fetch. The two helpers do base sixty four U R L encoding without padding, which is what J W T uses. Then mint builds the header, naming R S two five six and a key id, and the claims: issuer, audience, subject, issued at, and an expiry five minutes later. It joins the encoded header and claims with a dot, has openssl sign exactly that text with S H A two five six, and appends the signature. The claim names and format match GitHub's; only the key is ours.

## Files

- [`starter/issuer.py`](starter/issuer.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/issuer.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–7: at the top, openssl generates
   - Lines 8–13: the two helpers
   - Lines 14–22: then mint builds the header

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
