# m05l01 · Static IaC Scanning: Linting Terraform with Checkov

Module 5: Infrastructure as Code & Policy-as-Code · lesson 5.1 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m05l01)

**Goal:** You can read Checkov findings on a Terraform file, explain the logic behind a check such as CKV_AWS_24, wire the scan's exit code into a pipeline gate, and add a custom YAML check.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l01-02](m05l01-02/) | main.tf: three findings in twenty-two lines | Read along |
| [m05l01-03](m05l01-03/) | The logic behind CKV_AWS_24, applied to four groups | Graded |
| [m05l01-04](m05l01-04/) | The exit code is the gate | Graded |
| [m05l01-05](m05l01-05/) | A custom check in Checkov's YAML policy format | Checker |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Extend the check and the gate

1. Add a group with protocol "-1", ports 0 to 0, from 0.0.0.0/0. Predict, then run check_sg.py
2. Give exposes_ssh a port argument and add CKV_AWS_25, the same test for RDP on port 3389
3. Make gate.sh stop at the first file that fails and print that file's name

> **Hint:** Ports 0 to 0 do not contain 22, so only the protocol test can catch it. In bash, test $? straight after the scan.

## Check yourself

- The admin security group never mentions port twenty-two. Why does CKV_AWS_24 still fail it?
- A pipeline runs checkov with --soft-fail. What happens to a pull request that opens SSH to 0.0.0.0/0, and why?
- A security group's CIDR comes from a variable set in another repository. Why might a static scan pass it anyway?
- Why is a #checkov:skip comment inside the resource better than --skip-check on the command line?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
