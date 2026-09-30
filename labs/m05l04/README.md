# m05l04 · Continuous IaC Drift Detection & State Protection

Module 5: Infrastructure as Code & Policy-as-Code · lesson 5.4 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m05l04)

**Goal:** You can detect drift between Terraform state and live cloud resources, handle plan exit codes correctly in a scheduled job, find secrets stored in state, and harden a remote state backend.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l04-02](m05l04-02/) | What a refresh compares: state against the cloud | Graded |
| [m05l04-03](m05l04-03/) | The nightly job: reading exit codes correctly | Graded |
| [m05l04-05](m05l04-05/) | Finding the secrets in a state file | Graded |
| [m05l04-06](m05l04-06/) | backend.tf: an encrypted, locked, versioned home | Checker |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Break the job, then fix it

1. Delete the 443 rule from describe-security-groups.json; predict drift.py's output, then run it
2. Add set -e as the first line of ci.sh, run it, and explain why no drift report prints
3. Extend state_secrets.py to flag attributes named password or private_key that lack a path

> **Hint:** With set -e a failing command aborts the script; capture the code with: cmd || rc=$?

## Check yourself

- A nightly job runs terraform plan -detailed-exitcode and marks the run green whenever the exit code is not 2. What happens on the night the cloud credentials expire?
- An engineer says the database password is safe because its variable is declared sensitive = true. What does the state file show, and why?
- The drift report shows port 22 open to 0.0.0.0/0 with the description temp debug. Why is running terraform apply straight away not automatically the right response?
- Which backend setting stops two pipelines corrupting state by writing at the same time, and what does versioning the state bucket add on top?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
