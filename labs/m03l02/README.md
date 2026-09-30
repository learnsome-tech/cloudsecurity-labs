# m03l02 · Pre-Commit Secret Scanning with Gitleaks & Entropy

Module 3: CI/CD Security & Shift-Left Automation · lesson 3.2 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m03l02)

**Goal:** You can write a gitleaks rule that combines a token pattern with an entropy floor, enforce it in a pre-commit hook, and respond correctly when a secret reaches git history.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l02-02](m03l02-02/) | Measuring randomness with Shannon entropy | Graded |
| [m03l02-03](m03l02-03/) | A gitleaks rule for an internal token format | Read along |
| [m03l02-04](m03l02-04/) | Applying the same rule to a staged diff | Graded |
| [m03l02-05](m03l02-05/) | A pre-commit hook that refuses the commit | Graded |
| [m03l02-06](m03l02-06/) | Deleted from the file, still in the history | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Break the scanner on purpose

1. Delete the fixtures allowlist from scan_staged.py. Predict the findings, then run it.
2. Add a UUID line to staged.diff. Is it reported? Name the check that stops it.
3. In hook.sh, commit exmp_ plus 32 copies of one letter. Which check lets it through?
4. Extend history.sh with git show on the first commit and read the token back.

> **Hint:** The checks run in order: keyword, pattern, entropy, allowlist. Ask which one fails first.

## Check yourself

- Why does a UUID score above three and a half bits of entropy, yet never get reported by the token rule?
- A developer deletes a leaked token in a follow-up commit. Which command from the lesson proves it is still recoverable, and how?
- Every developer has the pre-commit hook installed. Why must the same scan still run in the pipeline?
- Why rotate a leaked key before rewriting the git history, rather than after?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
