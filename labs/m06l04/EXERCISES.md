# Exercises — Cloud Security Posture Management & Remediation

Lesson `m06l04` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m06l04)

## Exercise 1: Add a control and stress the guardrails

1. Add a control for AWS::EC2::Volume that fails when configuration.encrypted is false
2. Set MAX_CHANGES = 1 in remediate.py; predict the output, then run it
3. Give vendor-rdp a 0.0.0.0/1 range. Should it fail? Make the control agree with you
4. Ticket any failing resource that has no owner tag instead of fixing it

> **Hint**: Add a volume item to config-items.json with a configuration of {"encrypted": false}.


---

© LearnSome.tech · support@iwantto.learnsome.tech
