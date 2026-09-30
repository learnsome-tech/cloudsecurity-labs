# m03l03-02 · A data access module with four queries

**Lesson:** [Static Application Security Testing with Semgrep](https://learnsome.tech/learn/cloudsecurity-course/m03l03) (lesson 3.3, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Read along

## Goal

You can explain why syntax-aware SAST beats text matching, read and write a Semgrep rule for SQL built from strings, and route findings through an owned asset inventory.

In the lesson: Here is a small data access module using psycopg, the Postgres driver. Four functions, and between them they cover the cases that matter. The first function formats the user id straight into the SQL with the percent operator. That is injectable. The second looks similar but is safe: the percent s sits inside the string as a placeholder, and the value is passed separately as a parameter, so the driver treats it as a value and never as SQL. Next, search builds the query into a variable on one line and executes it on the next. Still injectable, just harder to spot. Last, row count has an old line commented out, and a new line that uses an f string with the table name. The comment is harmless. The f string is not.

## Files

- [`starter/db.py`](starter/db.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/db.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: The first function formats
   - Lines 6–9: The second looks similar
   - Lines 10–14: search builds the query
   - Lines 15–19: row count has an old line

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
