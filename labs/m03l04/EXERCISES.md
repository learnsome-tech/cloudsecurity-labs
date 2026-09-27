# Exercises — Software Composition Analysis with Trivy

Lesson `m03l04` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l04)

## Exercise 1: Move the pins and the dates

1. Pin requests==2.31.0 and rerun sca_match.py. Which finding remains, and why?
2. Set urllib3 to 2.0.3. Predict which pair of OSV events matches, then run it.
3. Change the waiver to exp:2026-12-31 and rerun sca_gate.py. What changed?
4. Add CVE-2023-32681 to .trivyignore with no date. Is that a good waiver? Why not?

> **Hint**: The lockfile pins urllib3 separately: bumping requests does not move it until pip-compile runs again.


---

© LearnSome.tech · support@iwantto.learnsome.tech
