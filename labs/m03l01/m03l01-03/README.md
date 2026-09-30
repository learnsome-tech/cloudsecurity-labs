# m03l01-03 · A pull request workflow with three gates

**Lesson:** [Shift-Left Security Principles & Automated Pipeline Gates](https://learnsome.tech/learn/cloudsecurity-course/m03l01) (lesson 3.1, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Checker

## Goal

You can design pull request gates that block new security errors and map each pipeline control to a change management process.

In the lesson: Here is a GitHub Actions workflow that runs on every pull request aimed at main. The permissions block gives the job read access to the code and nothing else, so a compromised step cannot push or publish. Checkout fetches the full history, because gitleaks looks only at the commits between main and this branch, and it needs both ends to exist. Redact keeps any secret it finds out of the build log, which is often readable by more people than the repository is. Next, Semgrep runs twice: once on the branch and once on main, each writing a SARIF file. SARIF is the standard JSON format most scanners can emit. Then the last step hands both files to a small gate script. One setting lives outside this file: the job only blocks a merge if branch protection lists it as a required check.

## Files

- [`starter/security.yml`](starter/security.yml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-03/starter`
2. Read `security.yml` the way the lesson builds it:
   - Lines 1–6: runs on every pull request
   - Lines 7–15: gitleaks looks only at
   - Lines 16–20: Semgrep runs twice
   - Lines 21–22: the last step hands
3. Notes from the lesson:
   - Line 6: Read-only token: a compromised step cannot push
   - Line 15: --redact keeps the secret out of the build log
4. Edit `security.yml` and check it: `actionlint security.yml`.
5. Check it from the repository root: `./check m03l01-03`.

## How to check

`./check m03l01-03` copies `starter/` into a scratch directory and runs `actionlint security.yml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it checks the GitHub Actions workflow with actionlint (its shellcheck and pyflakes integrations are off, as on the site). The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
