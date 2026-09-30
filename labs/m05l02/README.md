# m05l02 · Policy-as-Code Architecture: OPA & Rego Syntax

Module 5: Infrastructure as Code & Policy-as-Code · lesson 5.2 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m05l02)

**Goal:** You can read a Rego policy, predict its decision for a given input including undefined results, and query a decision service so that the caller fails closed.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l02-02](m05l02-02/) | buckets.rego: two allow rules and a deny set | Read along |
| [m05l02-04](m05l02-04/) | A line-by-line Python mirror of the policy | Graded |
| [m05l02-05](m05l02-05/) | The caller's side: querying the decision API | Graded |
| [m05l02-06](m05l02-06/) | buckets_test.rego: policy gets unit tests | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Make the decision fail closed by design

1. Predict, then check: drop .get() from rule_one and run rules.py on the svc-backup input
2. Write decide(i) returning allowed and reasons: allowed only if allow and deny is empty
3. Serve decide at platform/buckets/decision and make pep.py read only that field

> **Hint:** allowed = allow(i) and not deny(i). Keep the client strict: anything but True is a deny.

## Check yourself

- Amara is on the platform team and deletes a bucket without MFA. allow is true and deny holds a message. What should the caller do, and what does that suggest about the policy's design?
- A client posts to /v1/data/platform/bucket/allow, missing an s, and receives {}. What does that response mean, and how should the client treat it?
- What would a stranger's request return from data.platform.buckets.allow if the line default allow := false were deleted?
- The backup service's request has no user.team field. Why does the first allow rule not raise an error in Rego?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
