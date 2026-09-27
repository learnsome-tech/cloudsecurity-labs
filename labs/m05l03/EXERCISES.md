# Exercises — Enforcing OPA Guardrails on Terraform Plan Payloads

Lesson `m05l03` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m05l03)

## Exercise 1: Add a data sovereignty rule

1. Add a rule to guard.py: restricted data may only be planned in region eu-west-2
2. Set the region in plan-fixed.json to us-east-1; predict which addresses fail, then run it
3. Skip no-op changes in the encryption rule, rerun plan-fixed.json and note what you gave up

> **Hint**: The region is plan['configuration']['provider_config']['aws']['expressions']['region'].


---

© LearnSome.tech · support@iwantto.learnsome.tech
