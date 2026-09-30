# m03l02-03 · A gitleaks rule for an internal token format

**Lesson:** [Pre-Commit Secret Scanning with Gitleaks & Entropy](https://learnsome.tech/learn/cloudsecurity-course/m03l02) (lesson 3.2, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Read along

## Goal

You can write a gitleaks rule that combines a token pattern with an entropy floor, enforce it in a pre-commit hook, and respond correctly when a secret reaches git history.

In the lesson: This is a real gitleaks configuration file. The extend block, with use default set to true, keeps every built in rule and adds ours on top; leave it out and your file replaces the defaults. The custom rule describes an internal token format: the prefix exmp and an underscore, then thirty two letters or digits. Secret group one tells gitleaks which capture group is the secret, and the entropy of that group has to reach three and a half bits. Keywords are a cheap prefilter: gitleaks only runs the regular expression on content containing one of them, which keeps scans of large histories fast. The global allowlist skips files under the test fixtures folder, where fake tokens are expected. Keep allowlists narrow. A path pattern of dot star would quietly switch the whole scanner off.

## Files

- [`starter/.gitleaks.toml`](starter/.gitleaks.toml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/.gitleaks.toml` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: The extend block
   - Lines 5–12: The custom rule describes
   - Lines 13–16: The global allowlist skips
3. Notes from the lesson:
   - Line 12: Keywords: a cheap substring check before the regex runs

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
