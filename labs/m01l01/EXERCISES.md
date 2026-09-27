# Exercises — Shared Responsibility Model & Cloud Threat Landscapes

Lesson `m01l01` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m01l01)

## Exercise 1: Extend the audit

1. Add a group allowing tcp 3389 from 203.0.113.0/24. Predict the audit line, then run it.
2. Add a udp rule for ports 0 to 65535 from 0.0.0.0/0 to web. Is it reported? Should it be?
3. Add a bucket in eu-west-2 tagged customer-pii and one tagged internal with a null location.
4. Make the audit also report any rule whose range is wider than a /8, whatever the port.

> **Hint**: 203.0.113.0/24 is not inside any range in INTERNAL, so internal() returns False for it.


---

© LearnSome.tech · support@iwantto.learnsome.tech
