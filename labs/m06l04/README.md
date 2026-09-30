# m06l04 · Cloud Security Posture Management & Remediation

Module 6: Cloud Detection, Encryption & Compliance · lesson 6.4 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m06l04)

**Goal:** You can write posture controls against real AWS Config configuration items, decide which failures to fix automatically and which to hand to a person, and build remediation with exceptions, ownership and a blast radius limit.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l04-02](m06l04-02/) | A configuration item for one security group | Read along |
| [m06l04-03](m06l04-03/) | Two controls, written against the real fields | Read along |
| [m06l04-04](m06l04-04/) | Evaluating six resources | Graded |
| [m06l04-06](m06l04-06/) | A remediation plan with guardrails | Graded |
| [m06l04-07](m06l04-07/) | The same guardrails as an AWS Config remediation | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Add a control and stress the guardrails

1. Add a control for AWS::EC2::Volume that fails when configuration.encrypted is false
2. Set MAX_CHANGES = 1 in remediate.py; predict the output, then run it
3. Give vendor-rdp a 0.0.0.0/1 range. Should it fail? Make the control agree with you
4. Ticket any failing resource that has no owner tag instead of fixing it

> **Hint:** Add a volume item to config-items.json with a configuration of {"encrypted": false}.

## Check yourself

- The debug-temp group never mentions port 22, yet it fails the SSH control. What in its configuration item causes that?
- Why does the planner open a ticket for the Terraform-managed bastion group instead of revoking the rule itself?
- A remediation run suddenly plans forty changes. What should the tool do, and why?
- Which misconfigurations are good candidates for automatic remediation, and which should only raise an alert?
- An auditor asks how long the payroll bucket's public access block was off. Which record answers that?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
