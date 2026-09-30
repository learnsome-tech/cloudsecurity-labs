# m01l01 · Shared Responsibility Model & Cloud Threat Landscapes

Module 1: Multi-Account Cloud Architecture & Isolation · lesson 1.1 · Free · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m01l01)

**Goal:** You can say which security tasks stay with you in each cloud service model, audit a real security group export for admin ports open to the internet, and check bucket regions against a data residency rule.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l01-04](m01l01-04/) | A security group export in the real API format | Read along |
| [m01l01-05](m01l01-05/) | Which admin ports can the internet reach? | Graded |
| [m01l01-06](m01l01-06/) | Data residency: where do the buckets really live? | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Extend the audit

1. Add a group allowing tcp 3389 from 203.0.113.0/24. Predict the audit line, then run it.
2. Add a udp rule for ports 0 to 65535 from 0.0.0.0/0 to web. Is it reported? Should it be?
3. Add a bucket in eu-west-2 tagged customer-pii and one tagged internal with a null location.
4. Make the audit also report any rule whose range is wider than a /8, whatever the port.

> **Hint:** 203.0.113.0/24 is not inside any range in INTERNAL, so internal() returns False for it.

## Check yourself

- A team moves a web app from EC2 instances to a managed PaaS runtime. Which security tasks leave their list, and which stay?
- Why does a security group rule allowing 0.0.0.0/1 deserve the same alarm as one allowing 0.0.0.0/0?
- In the four Cs model, how can a hardened container image still be compromised through the cloud layer?
- GetBucketLocation returns null for a bucket tagged customer-pii under an EU-only rule. Is that a breach, and why?
- Staff share files through a SaaS drive you cannot configure. What does a CASB in API mode give you, and what can it not do that a proxy can?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
