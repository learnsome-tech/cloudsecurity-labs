# m06l03-05 · A key policy that separates admins from users

**Lesson:** [Envelope Encryption & Data Protection with KMS](https://learnsome.tech/learn/cloudsecurity-course/m06l03) (lesson 6.3, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Read along

## Goal

You can explain and carry out envelope encryption, work out whether a principal may use a KMS key from its key policy and IAM policies, and choose rotation, encryption context and deletion settings knowing what each one protects against.

In the lesson: This policy splits the two jobs. The first statement trusts I A M in the account, but only for administration: describe, get, list, enable, disable, putting the key policy and scheduling deletion. Encrypt and decrypt are not on that list, so an administrator can manage the key without reading the payroll. The second statement names the payroll app role directly and allows decrypt and generate data key, on one condition: the encryption context must say department equals payroll. Read the first statement again, though. Put key policy is on it. An administrator who can rewrite the policy can add themselves to the second statement tomorrow. The separation is only as strong as the list of people who can edit the policy, and every Put Key Policy call is worth an alert.

## Files

- [`starter/key-policy.json`](starter/key-policy.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/key-policy.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–8: the first statement
   - Lines 9–16: the second statement

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l03-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
