# Exercises — Workload Identity Federation: Eliminating Static Keys

Lesson `m02l02` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l02)

## Exercise 1: Attack the trust policy and the validator

1. In trust_check.py add repo:example-org/payments-api:environment:staging; predict each column.
2. Change the org wildcard to repo:example-org/payments-api:* and predict which rows pass.
3. In tokens.py edit the exp claim instead of sub, re-encode, and name the check that fails.
4. Sign a token with a second openssl key pair and confirm validate rejects it.

> **Hint**: The signature covers the header and payload bytes, so any edit breaks it. A wildcard after the repository still admits pull requests.


---

© LearnSome.tech · support@iwantto.learnsome.tech
