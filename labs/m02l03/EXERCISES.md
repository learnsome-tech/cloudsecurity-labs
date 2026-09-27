# Exercises — Cross-Account AssumeRole Chains & Temporary STS

Lesson `m02l03` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l03)

## Exercise 1: Break and fix the cross-account rules

1. In cross_account.py, let may_assume also cover vendor-audit; predict which side refuses now.
2. In vendor.py give the attacker tenant the owner's ExternalId and explain what that proves.
3. Add an aws:PrincipalOrgID condition to prod-deploy's trust and pass the key in ctx.
4. Add an event to trail.json where prod-deploy assumes a third role; rerun the trace.

> **Hint**: The identity policy and the trust policy are separate gates. An ExternalId only helps because the vendor, not the tenant, chooses it.


---

© LearnSome.tech · support@iwantto.learnsome.tech
