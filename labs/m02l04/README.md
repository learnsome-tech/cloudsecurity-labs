# m02l04 · Least Privilege Enforcement & CIEM Architecture

Module 2: Cloud Identity & Zero-Trust Governance · lesson 2.4 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m02l04)

**Goal:** You can measure the gap between granted and used permissions, generate a right-sized policy from CloudTrail, and flag privilege escalation paths.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l04-02](m02l04-02/) | The reporting role, as it was first written | Read along |
| [m02l04-03](m02l04-03/) | Turning CloudTrail events into permissions | Read along |
| [m02l04-04](m02l04-04/) | Measuring the gap between granted and used | Graded |
| [m02l04-05](m02l04-05/) | Generating a policy from what was actually used | Graded |
| [m02l04-06](m02l04-06/) | Looking for privilege escalation paths | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Right-size a role and find a new path

1. Add an s3:DeleteObject event by reporting-app to trail-90d.json; predict the unused count.
2. In trail.py, stop widening object keys; rerun rightsize.py and compare the policy.
3. Add iam:PutRolePolicy as a new path in escalate.py and predict which roles it flags.
4. Replace s3:* in reporting-role.json with the used S3 actions and rerun unused.py.

> **Hint:** Only events whose session ARN names reporting-app count. iam:* in platform-ops matches every new IAM action you add.

## Check yourself

- The reporting role holds dozens of actions but used a handful in ninety days. Why is the unused set a risk even though nobody calls those actions?
- A policy generated from ninety days of CloudTrail is applied to a role that also runs the year-end close. What goes wrong, and how would you catch it first?
- The CI role has iam:PassRole, lambda:CreateFunction and lambda:InvokeFunction but no IAM write actions. Why is it flagged as an escalation path?
- A bucket policy allows every principal but limits it with an aws:PrincipalOrgID condition containing a mistyped organisation ID. What does Access Analyzer report, and why?
- Why does just-in-time access reduce risk compared with an engineer holding production admin permanently, even if that engineer is trustworthy?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
