<img src="https://learnsome.tech/logo.png" width="48" alt="LearnSome.tech">

# Cloud Security & DevSecOps Engineering

6 modules, 28 lessons: Multi-Account Cloud Architecture & Isolation; Cloud Identity & Zero-Trust Governance; CI/CD Security & Shift-Left Automation; Container & Kubernetes Runtime Defense; Infrastructure as Code & Policy-as-Code; Cloud Detection, Encryption & Compliance.

## Watch and read

- **Course page**: [https://learnsome.tech/courses/cloudsecurity-course](https://learnsome.tech/courses/cloudsecurity-course)
- **Video player**: [https://learnsome.tech/courses/cloudsecurity-course/watch](https://learnsome.tech/courses/cloudsecurity-course/watch)
- **Handbook PDF**: [https://learnsome.tech/handbooks/cloudsecurity/book.pdf](https://learnsome.tech/handbooks/cloudsecurity/book.pdf)
- **On-site handbook**: [https://learnsome.tech/courses/cloudsecurity-course/book](https://learnsome.tech/courses/cloudsecurity-course/book)

## What is in this repository

This repository contains code artifacts, exercises and reference files for the lessons in this course.
28 lessons include a `labs/<lessonId>/` folder.
Each folder is named after the lesson identifier (e.g. `labs/m01l01/`) and contains the
artifact files shown in the course video, an `EXERCISES.md` with hands-on tasks, and
sub-directories named by artifact reference (e.g. `m01l01-02/`).

## Lessons

| # | Lesson | Watch | Labs | Handbook |
|---|--------|-------|------|----------|
| | **Multi-Account Cloud Architecture & Isolation** | | | |
| 1 | Shared Responsibility Model & Cloud Threat Landscapes | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m01l01) | [labs/m01l01/](labs/m01l01/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-1-1) |
| 2 | AWS Organizations, Account Hierarchies & Azure Management Groups | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m01l02) | [labs/m01l02/](labs/m01l02/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-1-2) |
| 3 | Service Control Policies & Guardrail Architecture | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m01l03) | [labs/m01l03/](labs/m01l03/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-1-3) |
| 4 | Security Landing Zones & Centralized Egress Inspection | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m01l04) | [labs/m01l04/](labs/m01l04/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-1-4) |
| 5 | Cloud Network Isolation: VPC Peering & PrivateLink | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m01l05) | [labs/m01l05/](labs/m01l05/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-1-5) |
| | **Cloud Identity & Zero-Trust Governance** | | | |
| 6 | Cloud IAM Architecture & Permission Boundaries | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l01) | [labs/m02l01/](labs/m02l01/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-2-1) |
| 7 | Workload Identity Federation: Eliminating Static Keys | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l02) | [labs/m02l02/](labs/m02l02/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-2-2) |
| 8 | Cross-Account AssumeRole Chains & Temporary STS | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l03) | [labs/m02l03/](labs/m02l03/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-2-3) |
| 9 | Least Privilege Enforcement & CIEM Architecture | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l04) | [labs/m02l04/](labs/m02l04/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-2-4) |
| 10 | Zero-Trust Network Access & IdP Federation | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l05) | [labs/m02l05/](labs/m02l05/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-2-5) |
| | **CI/CD Security & Shift-Left Automation** | | | |
| 11 | Shift-Left Security Principles & Automated Pipeline Gates | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l01) | [labs/m03l01/](labs/m03l01/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-3-1) |
| 12 | Pre-Commit Secret Scanning with Gitleaks & Entropy | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l02) | [labs/m03l02/](labs/m03l02/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-3-2) |
| 13 | Static Application Security Testing with Semgrep | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l03) | [labs/m03l03/](labs/m03l03/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-3-3) |
| 14 | Software Composition Analysis with Trivy | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l04) | [labs/m03l04/](labs/m03l04/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-3-4) |
| 15 | Supply Chain Security: SBOMs & Cosign Signing | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l05) | [labs/m03l05/](labs/m03l05/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-3-5) |
| | **Container & Kubernetes Runtime Defense** | | | |
| 16 | Container Hardening: Distroless & Rootless | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m04l01) | [labs/m04l01/](labs/m04l01/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-4-1) |
| 17 | Kubernetes Pod Security Standards: Baseline & Restricted | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m04l02) | [labs/m04l02/](labs/m04l02/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-4-2) |
| 18 | Kubernetes NetworkPolicies & Microsegmentation | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m04l03) | [labs/m04l03/](labs/m04l03/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-4-3) |
| 19 | Runtime Anomaly Detection with Falco & eBPF | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m04l04) | [labs/m04l04/](labs/m04l04/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-4-4) |
| 20 | Securing the Kubernetes Control Plane & Node Components | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m04l05) | [labs/m04l05/](labs/m04l05/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-4-5) |
| | **Infrastructure as Code & Policy-as-Code** | | | |
| 21 | Static IaC Scanning: Linting Terraform with Checkov | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m05l01) | [labs/m05l01/](labs/m05l01/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-5-1) |
| 22 | Policy-as-Code Architecture: OPA & Rego Syntax | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m05l02) | [labs/m05l02/](labs/m05l02/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-5-2) |
| 23 | Enforcing OPA Guardrails on Terraform Plan Payloads | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m05l03) | [labs/m05l03/](labs/m05l03/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-5-3) |
| 24 | Continuous IaC Drift Detection & State Protection | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m05l04) | [labs/m05l04/](labs/m05l04/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-5-4) |
| | **Cloud Detection, Encryption & Compliance** | | | |
| 25 | CloudTrail Logging, Integrity Validation & Athena | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m06l01) | [labs/m06l01/](labs/m06l01/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-6-1) |
| 26 | Threat Detection with GuardDuty & Anomaly Analytics | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m06l02) | [labs/m06l02/](labs/m06l02/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-6-2) |
| 27 | Envelope Encryption & Data Protection with KMS | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m06l03) | [labs/m06l03/](labs/m06l03/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-6-3) |
| 28 | Cloud Security Posture Management & Remediation | [▶](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m06l04) | [labs/m06l04/](labs/m06l04/) | [§](https://learnsome.tech/courses/cloudsecurity-course/book#lesson-6-4) |

## Exercises

Each lesson folder contains an `EXERCISES.md` with hands-on tasks drawn directly from the course material.
Open the file for a lesson to see the tasks and, where provided, hints.

---

© LearnSome.tech · support@iwantto.learnsome.tech
