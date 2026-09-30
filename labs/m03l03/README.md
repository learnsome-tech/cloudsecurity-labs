# m03l03 · Static Application Security Testing with Semgrep

Module 3: CI/CD Security & Shift-Left Automation · lesson 3.3 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m03l03)

**Goal:** You can explain why syntax-aware SAST beats text matching, read and write a Semgrep rule for SQL built from strings, and route findings through an owned asset inventory.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l03-02](m03l03-02/) | A data access module with four queries | Read along |
| [m03l03-03](m03l03-03/) | The grep approach, and why developers stop reading it | Graded |
| [m03l03-04](m03l03-04/) | Asking the syntax tree instead | Graded |
| [m03l03-05](m03l03-05/) | The same check as a Semgrep rule | Checker |
| [m03l03-08](m03l03-08/) | Joining the inventory to the scan results | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Stretch the scanner and the inventory

1. Change search() in db.py to build its query with .format(). Predict ast_scan.py, then run it.
2. Move the query building into a helper function. Does ast_scan.py still see it? Why not?
3. Add promo-site to inventory.csv with an owner. Predict its new line in coverage.py.
4. Add a nosemgrep comment to line 18 of db.py and explain why ast_scan.py ignores it.

> **Hint:** The scanner only follows assignments inside the same function, and comments never reach the tree.

## Check yourself

- Why did the regex scanner flag the find_by_email query even though it is safe?
- Why can the row_count function not be fixed by passing the table name as a query parameter?
- The coverage report says a decommissioned repository is still producing scan results. What does that tell you, and what should happen next?
- In asset management terms, what decides who receives a SAST finding, and what decides how urgently it must be fixed?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
