# Exercises — Security Landing Zones & Centralized Egress Inspection

Lesson `m01l04` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m01l04)

## Exercise 1: Tighten the checks

1. Change after/ authorization-mode to AlwaysAllow,RBAC. Predict cis.py, then fix the rule logic.
2. Add a rule that audit-log-path must be present, using a new wanted value.
3. Add files.pythonhosted.org to ALLOW and a host that should not match it. Predict both.
4. Change sni.py to print which ALLOW target matched each passing name.

> **Hint**: wanted in value.split(',') finds RBAC in AlwaysAllow,RBAC; the benchmark also forbids AlwaysAllow.


---

© LearnSome.tech · support@iwantto.learnsome.tech
