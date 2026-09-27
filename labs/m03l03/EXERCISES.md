# Exercises — Static Application Security Testing with Semgrep

Lesson `m03l03` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l03)

## Exercise 1: Stretch the scanner and the inventory

1. Change search() in db.py to build its query with .format(). Predict ast_scan.py, then run it.
2. Move the query building into a helper function. Does ast_scan.py still see it? Why not?
3. Add promo-site to inventory.csv with an owner. Predict its new line in coverage.py.
4. Add a nosemgrep comment to line 18 of db.py and explain why ast_scan.py ignores it.

> **Hint**: The scanner only follows assignments inside the same function, and comments never reach the tree.


---

© LearnSome.tech · support@iwantto.learnsome.tech
