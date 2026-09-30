# m06l03-06 · The authorisation rule, written as code

**Lesson:** [Envelope Encryption & Data Protection with KMS](https://learnsome.tech/learn/cloudsecurity-course/m06l03) (lesson 6.3, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Read along

## Goal

You can explain and carry out envelope encryption, work out whether a principal may use a KMS key from its key policy and IAM policies, and choose rotation, encryption context and deletion settings knowing what each one protects against.

In the lesson: To test a policy like that before it goes live, it helps to write the rule down as code. This is a simplified model: no service control policies, no grants, and only string equals conditions. The module loads the key policy and each role's I A M statements. Effects collects the effect of every statement that names this principal, or applies to it because it has no principal at all, covers the action with a wildcard match, and has every condition satisfied by the request context. Decide applies the order. Any deny anywhere wins. Otherwise, an allow in the key policy that names the role is enough on its own. Otherwise, the key policy must trust the account root and an I A M policy must allow the action. Anything else is an implicit deny.

## Files

- [`starter/kmsauth.py`](starter/kmsauth.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/kmsauth.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: the module loads
   - Lines 5–11: effects collects
   - Lines 12–22: decide applies the order

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l03-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
