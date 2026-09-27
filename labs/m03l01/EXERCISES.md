# Exercises — Shift-Left Security Principles & Automated Pipeline Gates

Lesson `m03l01` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l01)

## Exercise 1: Tune the gate and read the audit trail

1. Add the app/db.py SQL finding to main.sarif. Predict the gate's verdict, then run it.
2. Put the line number into the gate's key, rerun, and explain which findings changed state.
3. In backout.sh, run git show --stat on the revert commit and read what it changed.

> **Hint**: The gate counts per rule and file, so a finding main already has stays existing even when it moves.


---

© LearnSome.tech · support@iwantto.learnsome.tech
