# m03l03-05 · The same check as a Semgrep rule

**Lesson:** [Static Application Security Testing with Semgrep](https://learnsome.tech/learn/cloudsecurity-course/m03l03) (lesson 3.3, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Checker

## Goal

You can explain why syntax-aware SAST beats text matching, read and write a Semgrep rule for SQL built from strings, and route findings through an owned asset inventory.

In the lesson: Semgrep is not installed on this machine, so here is its rule file rather than a run. The header gives an id, the language, a severity, and a message that tells the developer how to fix it, not just what is wrong. The metadata maps it to C W E eighty nine, SQL injection. Pattern either means any branch may match. Dollar CUR is a metavariable: it matches any expression, so the rule works whatever the cursor is called. Three dots inside quotes match any string literal, and three dots as an argument match any arguments. The last branch handles the search function: pattern inside finds a formatted string assigned to a variable, and three dots on their own line mean any statements in between, followed by execute on that same variable. You would run it with semgrep scan, dash dash config, and the rule file.

## Files

- [`starter/sql-format.yml`](starter/sql-format.yml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-05/starter`
2. Read `sql-format.yml` the way the lesson builds it:
   - Lines 1–9: The header gives an id
   - Lines 10–13: Pattern either means
   - Lines 14–18: The last branch handles
3. Notes from the lesson:
   - Line 11: $CUR: a metavariable, any expression
   - Line 17: ... on its own line: any statements in between
4. Edit `sql-format.yml` and check it: `yamllint sql-format.yml`.
5. Check it from the repository root: `./check m03l03-05`.

## How to check

`./check m03l03-05` copies `starter/` into a scratch directory and runs `yamllint sql-format.yml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it lints the YAML with yamllint's `relaxed` rules: it passes when there are no errors. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
