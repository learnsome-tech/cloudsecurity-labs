# m06l04-07 · The same guardrails as an AWS Config remediation

**Lesson:** [Cloud Security Posture Management & Remediation](https://learnsome.tech/learn/cloudsecurity-course/m06l04) (lesson 6.4, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Read along

## Goal

You can write posture controls against real AWS Config configuration items, decide which failures to fix automatically and which to hand to a person, and build remediation with exceptions, ownership and a blast radius limit.

In the lesson: The managed version is a Config rule with a remediation configuration, defined in the same Terraform as everything else. The rule here is restricted S S H, whose managed identifier is incoming S S H disabled. The target is a Systems Manager automation document owned by A W S that removes unrestricted access to port twenty two. Automatic is true, with three attempts a minute apart. The parameters pass the failing group's resource I D, and a dedicated role for the automation to assume, so remediation holds exactly the permissions it needs. Execution controls are the blast radius cap: at most ten percent of targets at once, and stop if ten percent fail. This rule would also revert the Terraform bastion, which is why the rule set and the Terraform owners have to agree.

## Files

- [`starter/restricted-ssh.tf`](starter/restricted-ssh.tf): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/restricted-ssh.tf` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: the rule here is restricted
   - Lines 5–7: automatic is true
   - Lines 8–15: the parameters pass
   - Lines 16–22: execution controls are the blast radius cap

## How to check

**Read along.** Its Terraform configuration uses the `aws` provider, which needs a real cloud account. The lab sandbox has only the local, null and random providers.

There is nothing to check: `./check m06l04-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
