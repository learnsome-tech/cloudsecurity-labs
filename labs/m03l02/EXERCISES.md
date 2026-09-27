# Exercises — Pre-Commit Secret Scanning with Gitleaks & Entropy

Lesson `m03l02` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l02)

## Exercise 1: Break the scanner on purpose

1. Delete the fixtures allowlist from scan_staged.py. Predict the findings, then run it.
2. Add a UUID line to staged.diff. Is it reported? Name the check that stops it.
3. In hook.sh, commit exmp_ plus 32 copies of one letter. Which check lets it through?
4. Extend history.sh with git show on the first commit and read the token back.

> **Hint**: The checks run in order: keyword, pattern, entropy, allowlist. Ask which one fails first.


---

© LearnSome.tech · support@iwantto.learnsome.tech
