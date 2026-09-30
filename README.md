<p>
  <a href="https://learnsome.tech/courses/cloudsecurity-course">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/assets/wordmark-inverse.svg">
      <img src=".github/assets/wordmark.svg" alt="LearnSome.tech" width="260">
    </picture>
  </a>
</p>

# Cloud Security & DevSecOps Engineering

**Multi-Cloud IAM Zero-Trust, Pipeline CI/CD Scanning, Falco eBPF & Runtime Hardening**

6 modules, 28 lessons: Multi-Account Cloud Architecture & Isolation; Cloud Identity & Zero-Trust Governance; CI/CD Security & Shift-Left Automation; Container & Kubernetes Runtime Defense; Infrastructure as Code & Policy-as-Code; Cloud Detection, Encryption & Compliance. Advanced level, about 4 hours.

This repository holds the labs of the LearnSome.tech course [Cloud Security & DevSecOps Engineering](https://learnsome.tech/courses/cloudsecurity-course): each lab's starter files, a README with the goal, the steps and the expected output, and `./check`, which tests your work the way the site does.

## Start

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/learnsome-tech/cloudsecurity-labs?quickstart=1)

- **Codespaces:** the badge opens this repository in a dev container with Python 3.14.7, Terraform 1.16.4, kubeconform 0.8.0, hadolint 2.15.1, actionlint 1.7.12, ansible-core and yamllint and Git 2.34 (Ubuntu 22.04's), as in the site's lab sandbox.
- **On your machine:**

  ```sh
  git clone https://github.com/learnsome-tech/cloudsecurity-labs.git
  cd cloudsecurity-labs
  ./check m01l01-05
  ```

  You need Python 3 for `./check`, and for the labs themselves Python 3.14.7, Terraform 1.16.4, kubeconform 0.8.0, hadolint 2.15.1, actionlint 1.7.12, ansible-core and yamllint and Git 2.34 (Ubuntu 22.04's). Other versions mostly work, but only the sandbox's versions are sure to print what the site prints. VS Code's Dev Containers extension builds the same container as Codespaces (x86-64).

## Doing a lab

1. Open the lesson on LearnSome.tech and the lab folder beside it: `labs/<lesson>/<lab>/`. The lab README has the goal, the steps and the expected output.
2. Work in the lab's `starter/` folder.
3. From the repository root, run `./check <lab>` (for example `./check m01l01-05`), or `./check <lesson>` for all labs of a lesson, or `./check --all`. `./check --list` shows every lab and how it is checked.

`./check` runs your starter the way the site's lab sandbox does: in a scratch copy that is its working directory and `HOME`, with `LANG=C.UTF-8`, `TZ=UTC`, `input.txt` on standard input, 10 seconds and 256 KiB of output per stream. It then compares the output with the site's own rules, so a pass here is a pass on the site.

| Check | What `./check` does | Labs |
| --- | --- | --- |
| Graded | Runs the program and compares its output with `expected.txt`. | 68 |
| Checker | Validates the file with the checker the site uses (hadolint, kubeconform, actionlint, yamllint, `ansible-playbook --syntax-check` or `terraform validate`); passes when it finds no errors. | 16 |
| Runs, not graded | Runs the program and shows its output; the site gives no pass or fail, and the lab README says why. | 1 |
| Read along | Nothing to run here: the site shows the listing read-only, and the lab README says honestly what it needs (Docker, a cluster, a cloud account...). | 42 |

## What is published, and what is not

Every lab's starter is the code the lesson shows on screen, which is also what the lab editor on the site opens with. Where that code is the whole program, such as a recorded shell session or a script from the video, it is published as it is: it is the lesson content. Nothing beyond the lesson is published. There are no reference solutions and no answers to the lesson exercises, and nothing the site keeps private.

Pro lessons' labs are here as starters too. LearnSome.tech runs and grades your labs in its sandbox, hosts the videos and keeps your progress; running and grading a Pro lab on the site needs Pro.

## Modules and lessons

### Module 1: Multi-Account Cloud Architecture & Isolation

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 1.1 | [Shared Responsibility Model & Cloud Threat Landscapes](https://learnsome.tech/learn/cloudsecurity-course/m01l01) | [3 labs](labs/m01l01/) | Free |
| 1.2 | [AWS Organizations, Account Hierarchies & Azure Management Groups](https://learnsome.tech/learn/cloudsecurity-course/m01l02) | [3 labs](labs/m01l02/) | Free |
| 1.3 | [Service Control Policies & Guardrail Architecture](https://learnsome.tech/learn/cloudsecurity-course/m01l03) | [5 labs](labs/m01l03/) | Free |
| 1.4 | [Security Landing Zones & Centralized Egress Inspection](https://learnsome.tech/learn/cloudsecurity-course/m01l04) | [4 labs](labs/m01l04/) | Free |
| 1.5 | [Cloud Network Isolation: VPC Peering & PrivateLink](https://learnsome.tech/learn/cloudsecurity-course/m01l05) | [4 labs](labs/m01l05/) | Free |

### Module 2: Cloud Identity & Zero-Trust Governance

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 2.1 | [Cloud IAM Architecture & Permission Boundaries](https://learnsome.tech/learn/cloudsecurity-course/m02l01) | [4 labs](labs/m02l01/) | Pro |
| 2.2 | [Workload Identity Federation: Eliminating Static Keys](https://learnsome.tech/learn/cloudsecurity-course/m02l02) | [6 labs](labs/m02l02/) | Pro |
| 2.3 | [Cross-Account AssumeRole Chains & Temporary STS](https://learnsome.tech/learn/cloudsecurity-course/m02l03) | [6 labs](labs/m02l03/) | Pro |
| 2.4 | [Least Privilege Enforcement & CIEM Architecture](https://learnsome.tech/learn/cloudsecurity-course/m02l04) | [5 labs](labs/m02l04/) | Pro |
| 2.5 | [Zero-Trust Network Access & IdP Federation](https://learnsome.tech/learn/cloudsecurity-course/m02l05) | [4 labs](labs/m02l05/) | Pro |

### Module 3: CI/CD Security & Shift-Left Automation

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 3.1 | [Shift-Left Security Principles & Automated Pipeline Gates](https://learnsome.tech/learn/cloudsecurity-course/m03l01) | [3 labs](labs/m03l01/) | Pro |
| 3.2 | [Pre-Commit Secret Scanning with Gitleaks & Entropy](https://learnsome.tech/learn/cloudsecurity-course/m03l02) | [5 labs](labs/m03l02/) | Pro |
| 3.3 | [Static Application Security Testing with Semgrep](https://learnsome.tech/learn/cloudsecurity-course/m03l03) | [5 labs](labs/m03l03/) | Pro |
| 3.4 | [Software Composition Analysis with Trivy](https://learnsome.tech/learn/cloudsecurity-course/m03l04) | [5 labs](labs/m03l04/) | Pro |
| 3.5 | [Supply Chain Security: SBOMs & Cosign Signing](https://learnsome.tech/learn/cloudsecurity-course/m03l05) | [5 labs](labs/m03l05/) | Pro |

### Module 4: Container & Kubernetes Runtime Defense

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 4.1 | [Container Hardening: Distroless & Rootless](https://learnsome.tech/learn/cloudsecurity-course/m04l01) | [4 labs](labs/m04l01/) | Pro |
| 4.2 | [Kubernetes Pod Security Standards: Baseline & Restricted](https://learnsome.tech/learn/cloudsecurity-course/m04l02) | [5 labs](labs/m04l02/) | Pro |
| 4.3 | [Kubernetes NetworkPolicies & Microsegmentation](https://learnsome.tech/learn/cloudsecurity-course/m04l03) | [5 labs](labs/m04l03/) | Pro |
| 4.4 | [Runtime Anomaly Detection with Falco & eBPF](https://learnsome.tech/learn/cloudsecurity-course/m04l04) | [3 labs](labs/m04l04/) | Pro |
| 4.5 | [Securing the Kubernetes Control Plane & Node Components](https://learnsome.tech/learn/cloudsecurity-course/m04l05) | [5 labs](labs/m04l05/) | Pro |

### Module 5: Infrastructure as Code & Policy-as-Code

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 5.1 | [Static IaC Scanning: Linting Terraform with Checkov](https://learnsome.tech/learn/cloudsecurity-course/m05l01) | [4 labs](labs/m05l01/) | Pro |
| 5.2 | [Policy-as-Code Architecture: OPA & Rego Syntax](https://learnsome.tech/learn/cloudsecurity-course/m05l02) | [4 labs](labs/m05l02/) | Pro |
| 5.3 | [Enforcing OPA Guardrails on Terraform Plan Payloads](https://learnsome.tech/learn/cloudsecurity-course/m05l03) | [5 labs](labs/m05l03/) | Pro |
| 5.4 | [Continuous IaC Drift Detection & State Protection](https://learnsome.tech/learn/cloudsecurity-course/m05l04) | [4 labs](labs/m05l04/) | Pro |

### Module 6: Cloud Detection, Encryption & Compliance

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 6.1 | [CloudTrail Logging, Integrity Validation & Athena](https://learnsome.tech/learn/cloudsecurity-course/m06l01) | [6 labs](labs/m06l01/) | Pro |
| 6.2 | [Threat Detection with GuardDuty & Anomaly Analytics](https://learnsome.tech/learn/cloudsecurity-course/m06l02) | [5 labs](labs/m06l02/) | Pro |
| 6.3 | [Envelope Encryption & Data Protection with KMS](https://learnsome.tech/learn/cloudsecurity-course/m06l03) | [5 labs](labs/m06l03/) | Pro |
| 6.4 | [Cloud Security Posture Management & Remediation](https://learnsome.tech/learn/cloudsecurity-course/m06l04) | [5 labs](labs/m06l04/) | Pro |

**Free** lessons are open to anyone with a free LearnSome.tech account; **Pro** lessons need a Pro membership to watch, run and grade on the site.

## Licence

- **Code** (starter files, `check` and `.learnsome/`, the dev container and the workflows) is under the [MIT licence](LICENSE).
- **Written text** (the READMEs, lab instructions, lesson text, exercises and questions) is under [CC BY-NC-SA 4.0](LICENSE-text.md): share and adapt it with attribution to LearnSome.tech, not commercially, under the same licence.
- The LearnSome.tech name and logo are not covered by either licence.

## Contributing and security

This repository is generated from the course. Report a broken lab or a content error [as an issue](../../issues/new/choose); see [CONTRIBUTING.md](CONTRIBUTING.md). Security reports go to [SECURITY.md](SECURITY.md).

© 2026 LearnSome.tech
