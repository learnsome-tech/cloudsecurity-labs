# m05l03-02 · One resource change from the plan JSON

**Lesson:** [Enforcing OPA Guardrails on Terraform Plan Payloads](https://learnsome.tech/learn/cloudsecurity-course/m05l03) (lesson 5.3, module 5: Infrastructure as Code & Policy-as-Code) · Pro  
**Check:** Read along

## Goal

You can read a Terraform plan's JSON, map data types and classifications to protection methods, and write plan guardrails that enforce classification, encryption at rest and safe replacements.

In the lesson: Here is one entry from the plan, cut down to the fields that matter. First, the address names the resource. The actions list says delete, then create, so this is a replacement. Next, before and after show why. Someone switched storage encrypted from false to true, which is the right instinct, but R D S cannot encrypt an existing instance in place. Terraform will destroy the payroll database and build a new, empty one. Replace paths names the attribute that forced it, and after unknown lists what Terraform will only learn after apply. At the bottom, the configuration section records the provider's region, which is how a policy can check where the data is going to live.

## Files

- [`starter/plan-excerpt.json`](starter/plan-excerpt.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/plan-excerpt.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–8: the address names the resource
   - Lines 9–15: before and after show why
   - Lines 16–17: replace paths names the attribute
   - Lines 18–22: the configuration section records
3. Notes from the lesson:
   - Line 10: delete then create: this is a replacement

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
