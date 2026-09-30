# m05l03-06 · guardrails.rego: classify, encrypt, never destroy

**Lesson:** [Enforcing OPA Guardrails on Terraform Plan Payloads](https://learnsome.tech/learn/cloudsecurity-course/m05l03) (lesson 5.3, module 5: Infrastructure as Code & Policy-as-Code) · Pro  
**Check:** Read along

## Goal

You can read a Terraform plan's JSON, map data types and classifications to protection methods, and write plan guardrails that enforce classification, encryption at rest and safe replacements.

In the lesson: Here are three guardrails in Rego, each adding a message to the deny set. The first says every change that leaves something behind must carry a data classification tag; deletions are exempt because they leave nothing to label. The second says confidential or restricted data must be encrypted at rest. It fires only when neither the database flag, storage encrypted, nor the volume flag, encrypted, is true. The third looks at the before state. If the actions include delete and the object being destroyed was restricted, the plan is refused, however good the reason. Together they map onto the methods you just heard: classify first, encrypt at rest, and protect the availability of critical records. Conftest can run a policy like this against the plan file in a pipeline, using its namespace flag to find this package.

## Files

- [`starter/guardrails.rego`](starter/guardrails.rego): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/guardrails.rego` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–7: the first says every change
   - Lines 8–15: the second says confidential or restricted data
   - Lines 16–22: the third looks at the before state
3. Notes from the lesson:
   - Line 12: not ... not: fails only when neither flag is true

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l03-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
