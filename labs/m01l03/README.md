# m01l03 · Service Control Policies & Guardrail Architecture

Module 1: Multi-Account Cloud Architecture & Isolation · lesson 1.3 · Free · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m01l03)

**Goal:** You can predict whether a service control policy stack allows an API call by applying explicit deny first and then the allow-at-every-level rule, and design guardrails that enforce data residency without locking out your own platform team.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l03-02](m01l03-02/) | A region guardrail for data residency | Read along |
| [m01l03-03](m01l03-03/) | Does a statement match a request? | Read along |
| [m01l03-04](m01l03-04/) | Deny anywhere wins; allow must appear at every level | Read along |
| [m01l03-05](m01l03-05/) | Six calls through the guardrails of payments-prod | Graded |
| [m01l03-06](m01l03-06/) | One narrow allow list above the account | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Break and repair the guardrails

1. Add ssm:StartSession in eu-central-1 as developer to CALLS. Predict the verdict, then run.
2. Add kms:* and logs:* to AllowComputeAndStorage. Which narrow.py rows change?
3. Remove iam:* from the NotAction list and predict the iam:CreateRole row.
4. Write a DenyGuardDutyChanges SCP for Prod with a platform-admin exception, and test it.

> **Hint:** IAM requests carry aws:RequestedRegion us-east-1, so without the NotAction entry the region deny applies.

## Check yourself

- An account has FullAWSAccess attached, but its parent OU's only SCP allows ec2:* and s3:*. Can a role in the account call kms:Decrypt, and why?
- Why does the region-deny SCP use NotAction with a list of services such as iam:* and sts:*?
- A developer is allowed cloudtrail:StopLogging by an IAM policy. Which line of the check.py output shows what happens, and at which level?
- An SCP allows s3:* at every level, yet a role with no IAM policies attached calls s3:GetObject. What happens?
- Why is a deny-list strategy on top of FullAWSAccess usually safer to roll out than an allow-list strategy?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
