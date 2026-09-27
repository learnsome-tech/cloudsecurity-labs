# Exercises — Cloud Network Isolation: VPC Peering & PrivateLink

Lesson `m01l05` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m01l05)

## Exercise 1: Break and fix the routes

1. Add a pcx-3c between vpc-app and vpc-data with routes on both sides. Predict all three traces.
2. Add a 10.3.9.0/24 route in vpc-app that points at pcx-1a. Which route does lookup() pick now?
3. Give ml-sandbox a secondary block of 10.200.0.0/16. Does its overlap disappear? Why not?
4. In perimeter.yaml, add a statement allowing one partner bucket outside your organisation.

> **Hint**: Peering checks every associated block, so a new secondary range never removes an existing clash.


---

© LearnSome.tech · support@iwantto.learnsome.tech
