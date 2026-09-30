# m02l01 · Cloud IAM Architecture & Permission Boundaries

Module 2: Cloud Identity & Zero-Trust Governance · lesson 2.1 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m02l01)

**Goal:** You can evaluate an AWS IAM request in the real order, spot conditions that fail open, and cap role creation with a permissions boundary.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l01-03](m02l01-03/) | A policy evaluator you can read on one screen | Read along |
| [m02l01-04](m02l01-04/) | The developer policy under test | Read along |
| [m02l01-05](m02l01-05/) | Four requests against the developer policy | Graded |
| [m02l01-07](m02l01-07/) | An administrator role with a boundary attached | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Close both holes in the developer policy

1. In app-dev.json, drop s3:DeleteObject from AppData; allow it only with Bool MFA "true".
2. Predict all four verdicts, then rerun check_requests.py and explain the line that changed.
3. Add an iam:PermissionsBoundary StringEquals condition to BuildAppRoles and rerun.
4. Pass the boundary ARN in the CreateRole context and confirm the verdict returns to allow.

> **Hint:** An absent key fails any condition, so an Allow that needs MFA true fails closed. The boundary key goes in that request's ctx dict.

## Check yourself

- Priya's delete call is signed with long-term access keys, and her policy denies deletes when aws:MultiFactorAuthPresent is false. Why does the delete succeed?
- A role has AdministratorAccess attached and a permissions boundary that only allows S3 actions on one bucket. What happens when it calls iam:CreateUser, and why?
- Why do iam:CreateRole, iam:AttachRolePolicy and iam:PassRole together let a developer act as an administrator, and which condition key closes the gap?
- An engineer moved from testing to payments six months ago and still has test-account access. Which part of the identity lifecycle failed, and what should catch it?
- A service control policy blocks an action that the identity policy and boundary both allow. Which access control model does the SCP resemble, and what is the result?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
