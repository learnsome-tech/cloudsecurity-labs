# Exercises — Service Control Policies & Guardrail Architecture

Lesson `m01l03` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m01l03)

## Exercise 1: Break and repair the guardrails

1. Add ssm:StartSession in eu-central-1 as developer to CALLS. Predict the verdict, then run.
2. Add kms:* and logs:* to AllowComputeAndStorage. Which narrow.py rows change?
3. Remove iam:* from the NotAction list and predict the iam:CreateRole row.
4. Write a DenyGuardDutyChanges SCP for Prod with a platform-admin exception, and test it.

> **Hint**: IAM requests carry aws:RequestedRegion us-east-1, so without the NotAction entry the region deny applies.


---

© LearnSome.tech · support@iwantto.learnsome.tech
