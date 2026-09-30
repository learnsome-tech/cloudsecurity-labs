# m01l05 · Cloud Network Isolation: VPC Peering & PrivateLink

Module 1: Multi-Account Cloud Architecture & Isolation · lesson 1.5 · Free · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m01l05)

**Goal:** You can trace a packet through peered VPC route tables, spot CIDR overlaps that block peering, and choose between peering and PrivateLink by what each one exposes.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l05-02](m01l05-02/) | Three route tables and a hopeful route | Read along |
| [m01l05-03](m01l05-03/) | Tracing packets hop by hop | Graded |
| [m01l05-04](m01l05-04/) | Overlapping ranges: who can never peer | Graded |
| [m01l05-06](m01l05-06/) | A data perimeter from both sides of an endpoint | Checker |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Break and fix the routes

1. Add a pcx-3c between vpc-app and vpc-data with routes on both sides. Predict all three traces.
2. Add a 10.3.9.0/24 route in vpc-app that points at pcx-1a. Which route does lookup() pick now?
3. Give ml-sandbox a secondary block of 10.200.0.0/16. Does its overlap disappear? Why not?
4. In perimeter.yaml, add a statement allowing one partner bucket outside your organisation.

> **Hint:** Peering checks every associated block, so a new secondary range never removes an existing clash.

## Check yourself

- vpc-app has a route for 10.3.0.0/16 pointing at its peering connection to vpc-hub. Why does the packet still not reach vpc-data?
- Shared-services' primary range is 10.100.0.0/16, yet the overlap check refuses to let it peer with payments-dev. What caused that?
- A vendor's VPC overlaps yours, and you need one of their HTTPS APIs. Why is PrivateLink a better fit than peering here?
- The exports bucket denies requests whose aws:SourceVpce is not your endpoint. What does that stop, and what might it break?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
