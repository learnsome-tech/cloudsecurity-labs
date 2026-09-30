# m02l02-03 · The workflow side: permission to ask for a token

**Lesson:** [Workload Identity Federation: Eliminating Static Keys](https://learnsome.tech/learn/cloudsecurity-course/m02l02) (lesson 2.2, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Checker

## Goal

You can replace stored cloud keys with OIDC federation and write a trust policy that only the intended pipeline can satisfy.

In the lesson: On the GitHub side there is very little to it. The workflow runs on every push to main. The permissions block grants id token write, without which the job cannot request a token at all, and it keeps repository contents read only. Next, the job names an environment called production. That line matters more than it looks. When a job uses an environment, GitHub writes the environment into the subject claim instead of the branch, and an environment can require a named person to approve before the job starts. Finally the configure credentials action from A W S requests the token, calls S T S with the role A R N, and exports temporary keys for the steps after it. No secret appears anywhere in this file.

## Files

- [`starter/deploy.yml`](starter/deploy.yml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-03/starter`
2. Read `deploy.yml` the way the lesson builds it:
   - Lines 1–4: runs on every push to main
   - Lines 5–8: the permissions block
   - Lines 9–13: the job names an environment
   - Lines 14–20: the configure credentials action
3. Notes from the lesson:
   - Line 7: Without id-token: write the job cannot request a token
   - Line 13: The sub claim becomes ...:environment:production
4. Edit `deploy.yml` and check it: `actionlint deploy.yml`.
5. Check it from the repository root: `./check m02l02-03`.

## How to check

`./check m02l02-03` copies `starter/` into a scratch directory and runs `actionlint deploy.yml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it checks the GitHub Actions workflow with actionlint (its shellcheck and pyflakes integrations are off, as on the site). The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
