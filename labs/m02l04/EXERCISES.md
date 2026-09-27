# Exercises — Least Privilege Enforcement & CIEM Architecture

Lesson `m02l04` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l04)

## Exercise 1: Right-size a role and find a new path

1. Add an s3:DeleteObject event by reporting-app to trail-90d.json; predict the unused count.
2. In trail.py, stop widening object keys; rerun rightsize.py and compare the policy.
3. Add iam:PutRolePolicy as a new path in escalate.py and predict which roles it flags.
4. Replace s3:* in reporting-role.json with the used S3 actions and rerun unused.py.

> **Hint**: Only events whose session ARN names reporting-app count. iam:* in platform-ops matches every new IAM action you add.


---

© LearnSome.tech · support@iwantto.learnsome.tech
