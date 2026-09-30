# m03l01 · Shift-Left Security Principles & Automated Pipeline Gates

Module 3: CI/CD Security & Shift-Left Automation · lesson 3.1 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m03l01)

**Goal:** You can design pull request gates that block new security errors and map each pipeline control to a change management process.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l01-03](m03l01-03/) | A pull request workflow with three gates | Checker |
| [m03l01-04](m03l01-04/) | A gate that blocks new errors and tolerates old debt | Graded |
| [m03l01-05](m03l01-05/) | Version control as the change record and the backout | Runs, not graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Tune the gate and read the audit trail

1. Add the app/db.py SQL finding to main.sarif. Predict the gate's verdict, then run it.
2. Put the line number into the gate's key, rerun, and explain which findings changed state.
3. In backout.sh, run git show --stat on the revert commit and read what it changed.

> **Hint:** The gate counts per rule and file, so a finding main already has stays existing even when it moves.

## Check yourself

- Why does the gate compare findings by rule and file rather than by rule, file and line?
- The Semgrep job fails on a pull request but is not a required check in branch protection. What happens when someone clicks merge?
- Why is git revert a better backout than force pushing main back to the previous commit?
- A pull request widens an egress allow list. Which change management items should reviewers see before it merges?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
