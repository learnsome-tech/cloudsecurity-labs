# m02l03 · Cross-Account AssumeRole Chains & Temporary STS

Module 2: Cloud Identity & Zero-Trust Governance · lesson 2.3 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m02l03)

**Goal:** You can design cross-account role trust that resists the confused deputy, predict when STS refuses a hop, and trace a role chain through CloudTrail.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l03-02](m02l03-02/) | The target roles, as get-role describes them | Read along |
| [m02l03-03](m02l03-03/) | The rules STS applies to AssumeRole | Read along |
| [m02l03-04](m02l03-04/) | Four attempts to reach production | Graded |
| [m02l03-06](m02l03-06/) | The confused deputy, with and without the condition | Graded |
| [m02l03-07](m02l03-07/) | What an AssumeRole event records | Read along |
| [m02l03-08](m02l03-08/) | Walking a chain back to its origin | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Break and fix the cross-account rules

1. In cross_account.py, let may_assume also cover vendor-audit; predict which side refuses now.
2. In vendor.py give the attacker tenant the owner's ExternalId and explain what that proves.
3. Add an aws:PrincipalOrgID condition to prod-deploy's trust and pass the key in ctx.
4. Add an event to trail.json where prod-deploy assumes a third role; rerun the trace.

> **Hint:** The identity policy and the trust policy are separate gates. An ExternalId only helps because the vendor, not the tenant, chooses it.

## Check yourself

- The CI role's policy allows sts:AssumeRole on prod-deploy, but prod-deploy's trust policy names a different role. What does the call return, and which document must change?
- An attacker who is also a customer of your monitoring vendor enters your role ARN. Why does requiring sts:ExternalId stop the vendor from assuming your role for them?
- A job running as a role session asks for DurationSeconds 7200 on a role whose MaxSessionDuration is twelve hours. What happens, and why?
- Which CloudTrail field links an AssumeRole event to the later API calls made with the credentials it issued?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
