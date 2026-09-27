# Exercises — Continuous IaC Drift Detection & State Protection

Lesson `m05l04` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m05l04)

## Exercise 1: Break the job, then fix it

1. Delete the 443 rule from describe-security-groups.json; predict drift.py's output, then run it
2. Add set -e as the first line of ci.sh, run it, and explain why no drift report prints
3. Extend state_secrets.py to flag attributes named password or private_key that lack a path

> **Hint**: With set -e a failing command aborts the script; capture the code with: cmd || rc=$?


---

© LearnSome.tech · support@iwantto.learnsome.tech
