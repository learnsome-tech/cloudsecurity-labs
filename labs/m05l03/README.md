# m05l03 · Enforcing OPA Guardrails on Terraform Plan Payloads

Module 5: Infrastructure as Code & Policy-as-Code · lesson 5.3 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m05l03)

**Goal:** You can read a Terraform plan's JSON, map data types and classifications to protection methods, and write plan guardrails that enforce classification, encryption at rest and safe replacements.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l03-02](m05l03-02/) | One resource change from the plan JSON | Read along |
| [m05l03-03](m05l03-03/) | Three questions to ask any plan, answered with jq | Graded |
| [m05l03-06](m05l03-06/) | guardrails.rego: classify, encrypt, never destroy | Read along |
| [m05l03-07](m05l03-07/) | The guardrails against the plan | Graded |
| [m05l03-08](m05l03-08/) | The revised plan, and the violation that stays | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Add a data sovereignty rule

1. Add a rule to guard.py: restricted data may only be planned in region eu-west-2
2. Set the region in plan-fixed.json to us-east-1; predict which addresses fail, then run it
3. Skip no-op changes in the encryption rule, rerun plan-fixed.json and note what you gave up

> **Hint:** The region is plan['configuration']['provider_config']['aws']['expressions']['region'].

## Check yourself

- The payroll change only switched storage_encrypted from false to true. Why did the guardrail refuse the plan, and which plan fields show the cause?
- A policy denies any new EBS volume whose kms_key_id is null in the plan's after block. What goes wrong, and what should it test instead?
- UK payroll records are planned into a bucket in us-east-1. Which data protection consideration does that raise, and which securing method would a plan policy enforce?
- Billing must use card numbers, other systems must never hold them, and support staff see only the last four digits. Which two methods fit, and why is encryption at rest alone not enough?
- Why should a plan JSON build artefact be handled as confidential even when the infrastructure it describes holds only public data?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
