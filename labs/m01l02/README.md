# m01l02 · AWS Organizations, Account Hierarchies & Azure Management Groups

Module 1: Multi-Account Cloud Architecture & Isolation · lesson 1.2 · Free · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m01l02)

**Goal:** You can lay out an AWS organisation or Azure management group tree so each account limits blast radius, and work out which accounts an organisation path condition will let in.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l02-03](m01l02-03/) | The organisation tree as the API describes it | Read along |
| [m01l02-04](m01l02-04/) | Walking the tree to find misplaced accounts | Graded |
| [m01l02-05](m01l02-05/) | Placement is access: the organisation path condition | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Move accounts and predict the fallout

1. Move data-lake-prod under the Prod OU in org.json. Predict both programs' output, then run.
2. Nest a new OU inside Prod with an account in it. Does the Workloads pattern still match it?
3. Drop the trailing * from POLICY. Which accounts match now, and why?
4. Add a check to orgtree.py that warns when an account is more than five OUs below the root.

> **Hint:** Without a star, string_like is an exact comparison, and every path ends at the account's parent OU.

## Check yourself

- A developer's sandbox access key leaks. Why does a separate sandbox account contain the damage better than a separate IAM user in the production account?
- Why should the management account hold no workloads, even though it is the most trusted account in the organisation?
- data-lake-prod sits directly under the root. What two consequences did orgtree.py and orgpaths.py show?
- In Azure, what happens to a subscription created next year if someone holds Owner at the Tenant Root Group?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
