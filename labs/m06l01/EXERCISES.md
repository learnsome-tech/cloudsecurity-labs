# Exercises — CloudTrail Logging, Integrity Validation & Athena

Lesson `m06l01` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m06l01)

## Exercise 1: Extend the validator and the audit queries

1. In validate.py, delete a whole log file and make validate() report it as missing
2. Predict first: what should validation say if the intruder deletes digest.sig?
3. Add a jq query listing every forbidden request with its verb, resource and namespace
4. Add a RequestResponse rule for pods/exec to the policy; decide where in the order it goes

> **Hint**: sha256() raises FileNotFoundError for a deleted file: test Path.exists() before hashing.


---

© LearnSome.tech · support@iwantto.learnsome.tech
