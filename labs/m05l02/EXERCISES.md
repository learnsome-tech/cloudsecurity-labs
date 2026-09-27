# Exercises — Policy-as-Code Architecture: OPA & Rego Syntax

Lesson `m05l02` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m05l02)

## Exercise 1: Make the decision fail closed by design

1. Predict, then check: drop .get() from rule_one and run rules.py on the svc-backup input
2. Write decide(i) returning allowed and reasons: allowed only if allow and deny is empty
3. Serve decide at platform/buckets/decision and make pep.py read only that field

> **Hint**: allowed = allow(i) and not deny(i). Keep the client strict: anything but True is a deny.


---

© LearnSome.tech · support@iwantto.learnsome.tech
