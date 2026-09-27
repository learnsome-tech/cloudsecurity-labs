# Exercises — Cloud IAM Architecture & Permission Boundaries

Lesson `m02l01` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l01)

## Exercise 1: Close both holes in the developer policy

1. In app-dev.json, drop s3:DeleteObject from AppData; allow it only with Bool MFA "true".
2. Predict all four verdicts, then rerun check_requests.py and explain the line that changed.
3. Add an iam:PermissionsBoundary StringEquals condition to BuildAppRoles and rerun.
4. Pass the boundary ARN in the CreateRole context and confirm the verdict returns to allow.

> **Hint**: An absent key fails any condition, so an Allow that needs MFA true fails closed. The boundary key goes in that request's ctx dict.


---

© LearnSome.tech · support@iwantto.learnsome.tech
