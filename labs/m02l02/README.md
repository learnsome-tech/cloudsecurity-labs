# m02l02 · Workload Identity Federation: Eliminating Static Keys

Module 2: Cloud Identity & Zero-Trust Governance · lesson 2.2 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m02l02)

**Goal:** You can replace stored cloud keys with OIDC federation and write a trust policy that only the intended pipeline can satisfy.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l02-03](m02l02-03/) | The workflow side: permission to ask for a token | Checker |
| [m02l02-04](m02l02-04/) | The AWS side: a trust policy that pins the subject | Read along |
| [m02l02-05](m02l02-05/) | A stand-in issuer that signs tokens like GitHub | Read along |
| [m02l02-06](m02l02-06/) | Validating a token the way STS does | Read along |
| [m02l02-07](m02l02-07/) | Four tokens, one of them genuine | Graded |
| [m02l02-08](m02l02-08/) | Why the subject condition is the real defence | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Attack the trust policy and the validator

1. In trust_check.py add repo:example-org/payments-api:environment:staging; predict each column.
2. Change the org wildcard to repo:example-org/payments-api:* and predict which rows pass.
3. In tokens.py edit the exp claim instead of sub, re-encode, and name the check that fails.
4. Sign a token with a second openssl key pair and confirm validate rejects it.

> **Hint:** The signature covers the header and payload bytes, so any edit breaks it. A wildcard after the repository still admits pull requests.

## Check yourself

- A trust policy for GitHub's OIDC provider checks only the aud claim. Who can assume the role, and why does the token's valid signature not stop them?
- An attacker edits the sub claim inside a genuine token without re-signing it. Which check rejects the token, and why?
- A job gains environment: production and its deploys start failing with access denied. What changed in the token, and how should the trust policy change?
- Why is a leaked long-term access key harder to contain than a leaked set of federated session credentials?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
