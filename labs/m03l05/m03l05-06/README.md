# m03l05-06 · The same flow with cosign

**Lesson:** [Supply Chain Security: SBOMs & Cosign Signing](https://learnsome.tech/learn/cloudsecurity-course/m03l05) (lesson 3.5, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Read along

## Goal

You can produce and query CycloneDX SBOMs, sign and verify an image digest the way cosign does, and roll out signature enforcement as a controlled change.

In the lesson: Here is the same flow with cosign itself. The image is always addressed by digest, taken from the build step. Generate key pair writes cosign dot key, encrypted with a password, and cosign dot pub. Sign pushes the signature to the registry beside the image, and verify checks it. Attest wraps the S B O M in a signed in toto statement of type CycloneDX and attaches that too, and verify attestation checks it. Long lived keys are the hard part to protect, so in pipelines most teams use keyless signing instead. Cosign swaps the workflow's O I D C token for a short lived certificate from Fulcio, and records the signature in Rekor, a public transparency log. Verification then pins who is allowed to sign: the certificate identity must match this repository's workflows, and the issuer must be GitHub's token service.

## Files

- [`starter/cosign.sh`](starter/cosign.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/cosign.sh` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: always addressed by digest
   - Lines 2–6: Generate key pair writes
   - Lines 7–11: Attest wraps the
   - Lines 12–17: most teams use keyless signing
3. Notes from the lesson:
   - Line 16: Pin who may sign: this repository's workflows only

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l05-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
