# m03l04-03 · One advisory in OSV format

**Lesson:** [Software Composition Analysis with Trivy](https://learnsome.tech/learn/cloudsecurity-course/m03l04) (lesson 3.4, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Read along

## Goal

You can match pinned dependencies against OSV advisory ranges, gate a Trivy report with severity thresholds and expiring waivers, and place composition analysis within the four Cs of cloud native security.

In the lesson: Here is the other half: one advisory in OSV format, the open schema behind osv dot dev, which GitHub's advisory database also publishes in. The id is the GitHub advisory, and aliases links it to the C V E number. The affected block names the ecosystem and the package. The ranges are a list of events read in order: introduced at zero, fixed in one point twenty six point seventeen, introduced again at two point zero point zero, fixed in two point zero point six. So every one point x release before the fix is affected, and on the two branch only versions from two point zero point zero up to two point zero point five. The severity field comes from GitHub's review. A scanner that only read the first fixed event would miss the vulnerable two point x releases entirely.

## Files

- [`starter/GHSA-v845-jxx5-vc9f.json`](starter/GHSA-v845-jxx5-vc9f.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/GHSA-v845-jxx5-vc9f.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: The id is the GitHub advisory
   - Lines 5–6: The affected block
   - Lines 7–14: The ranges are a list
   - Lines 15–16: The severity field

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l04-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
