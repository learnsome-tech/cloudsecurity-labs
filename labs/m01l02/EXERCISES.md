# Exercises — AWS Organizations, Account Hierarchies & Azure Management Groups

Lesson `m01l02` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m01l02)

## Exercise 1: Move accounts and predict the fallout

1. Move data-lake-prod under the Prod OU in org.json. Predict both programs' output, then run.
2. Nest a new OU inside Prod with an account in it. Does the Workloads pattern still match it?
3. Drop the trailing * from POLICY. Which accounts match now, and why?
4. Add a check to orgtree.py that warns when an account is more than five OUs below the root.

> **Hint**: Without a star, string_like is an exact comparison, and every path ends at the account's parent OU.


---

© LearnSome.tech · support@iwantto.learnsome.tech
