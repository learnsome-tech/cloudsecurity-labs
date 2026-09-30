# m03l04-07 · Trivy at each layer

**Lesson:** [Software Composition Analysis with Trivy](https://learnsome.tech/learn/cloudsecurity-course/m03l04) (lesson 3.4, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Read along

## Goal

You can match pinned dependencies against OSV advisory ranges, gate a Trivy report with severity thresholds and expiring waivers, and place composition analysis within the four Cs of cloud native security.

In the lesson: Trivy is handy here because one tool reaches all four layers. For code, trivy fs scans the repository's lockfiles, and its secret scanner can run in the same pass. For the container, trivy image reads the operating system package database and the application dependencies inside the built image. Ignore unfixed drops findings that have no fixed version yet, which you cannot act on today, though someone should still know they exist. For the cluster, trivy config checks Kubernetes manifests and Helm charts for settings such as privileged containers, before they are applied. For the cloud layer, the same config scanner reads the Terraform that builds the account. Every command can write JSON or SARIF, which is what the gate you just saw and the pull request gate from earlier in this module consume. Exit code one turns a finding into a failed step.

## Files

- [`starter/scan.sh`](starter/scan.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/scan.sh` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: For code, trivy fs
   - Lines 4–7: For the container
   - Lines 8–10: For the cluster
   - Lines 11–13: For the cloud layer
   - Lines 14–16: Every command can write
3. Notes from the lesson:
   - Line 5: --ignore-unfixed: hide findings with no fix yet

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l04-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
