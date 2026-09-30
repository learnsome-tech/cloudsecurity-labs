# m02l05 · Zero-Trust Network Access & IdP Federation

Module 2: Cloud Identity & Zero-Trust Governance · lesson 2.5 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m02l05)

**Goal:** You can explain how a zero-trust broker decides each request from identity, group and device, and deprovision a user through SCIM so access ends mid-session.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l05-03](m02l05-03/) | The broker's decision, check by check | Read along |
| [m02l05-04](m02l05-04/) | A real HTTP server with a SCIM endpoint | Read along |
| [m02l05-05](m02l05-05/) | Five requests, five decisions | Graded |
| [m02l05-06](m02l05-06/) | Offboarding through SCIM, mid-session | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Extend the broker and its SCIM endpoint

1. Issue alice a token with iat one day earlier; predict the status and reason first.
2. Make do_PATCH accept op "Replace" and value "False" as a string, as some IdPs send.
3. Require a SCIM bearer token in do_PATCH and show an unauthenticated PATCH is refused.
4. Refuse devices whose owner differs from the token's sub, and test it with bob's laptop.

> **Hint:** In Python the string "False" is truthy, so compare it explicitly. The device owner is in devices.json.

## Check yourself

- Alice's token is still valid for forty minutes, yet her next request is refused after the SCIM PATCH. Which check refused it, and how would a VPN session behave differently?
- Bob edits the groups claim in his own token to payroll-admins. Why does the broker answer 401 instead of letting him in?
- Alice presents a perfect identity token but opens payroll on an unmanaged tablet. What does the broker decide, and why is identity alone not enough?
- An organisation uses SAML single sign-on for every app but has no SCIM. What goes wrong when someone leaves?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
