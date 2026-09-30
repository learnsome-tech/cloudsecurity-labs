# m01l04 · Security Landing Zones & Centralized Egress Inspection

Module 1: Multi-Account Cloud Architecture & Isolation · lesson 1.4 · Free · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m01l04)

**Goal:** You can describe the baseline a security landing zone gives every new account, review Kubernetes control plane and kubelet flags against CIS benchmark expectations, and explain what a centralised domain allow list really inspects and how it can be bypassed.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l04-03](m01l04-03/) | A control plane manifest that fails the CIS benchmark | Checker |
| [m01l04-04](m01l04-04/) | Checking the flags the way kube-bench does | Graded |
| [m01l04-06](m01l04-06/) | A domain allow list rule group | Read along |
| [m01l04-07](m01l04-07/) | Reading the server name from a real Client Hello | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Tighten the checks

1. Change after/ authorization-mode to AlwaysAllow,RBAC. Predict cis.py, then fix the rule logic.
2. Add a rule that audit-log-path must be present, using a new wanted value.
3. Add files.pythonhosted.org to ALLOW and a host that should not match it. Predict both.
4. Change sni.py to print which ALLOW target matched each passing name.

> **Hint:** wanted in value.split(',') finds RBAC in AlwaysAllow,RBAC; the benchmark also forbids AlwaysAllow.

## Check yourself

- Why must a vended workload account be unable to delete the CloudTrail events stored in the log archive account?
- cis.py reports authorization-mode AlwaysAllow as a failure. What would an authenticated user be able to do on that cluster, and why does RBAC not help?
- Spoke traffic reaches a central Network Firewall, but the domain allow list never drops anything from the spokes. Which setting is the most likely cause?
- Why was evilexample.com dropped when the allow list contains .example.com?
- Malware sends a Client Hello with the server name updates.example.com to an attacker's address. Why does a name-only allow list pass it, and what would stop it?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
