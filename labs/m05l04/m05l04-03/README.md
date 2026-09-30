# m05l04-03 · The nightly job: reading exit codes correctly

**Lesson:** [Continuous IaC Drift Detection & State Protection](https://learnsome.tech/learn/cloudsecurity-course/m05l04) (lesson 5.4, module 5: Infrastructure as Code & Policy-as-Code) · Pro  
**Check:** Graded

## Goal

You can detect drift between Terraform state and live cloud resources, handle plan exit codes correctly in a scheduled job, find secrets stored in state, and harden a remote state backend.

In the lesson: Scheduled drift detection lives or dies on how the job reads that exit code. This wrapper is what a nightly job does, with drift dot py standing in for terraform plan so it runs on a laptop; the comment shows the real command. Zero means clean. Two means drift, so the job opens a ticket carrying the report for the owning team. Anything else means the check itself failed, which is not the same as clean. The second call points at a cloud response that never arrived, the way expired credentials would leave you. Run both. The first reports the new rule. The second fails loudly instead of passing quietly. And watch for set minus e at the top of pipeline scripts: it aborts the job on exit code two, the one result you wanted to handle.

## Files

- [`starter/ci.sh`](starter/ci.sh): the listing from the lesson
- [`starter/command.txt`](starter/command.txt)
- [`starter/describe-security-groups.json`](starter/describe-security-groups.json)
- [`starter/drift.py`](starter/drift.py)
- [`starter/terraform.tfstate`](starter/terraform.tfstate)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-03/starter`
2. Read `ci.sh` the way the lesson builds it:
   - Lines 1–3: the comment shows the real command
   - Lines 4–13: zero means clean
   - Lines 14–15: the second call points at a cloud response
3. Run it: `bash ci.sh`.
4. Check it from the repository root: `./check m05l04-03`.

## Expected output

```text
describe-security-groups.json: drift, ticket opened for the owning team
+ aws_security_group.web ingress ('tcp', 22, 22, '0.0.0.0/0')
state serial 42: drift
describe-never-arrived.json: check failed, status unknown, paging on-call
FileNotFoundError: [Errno 2] No such file or directory: 'describe-never-arrived.json'
```

## How to check

`./check m05l04-03` copies `starter/` into a scratch directory and runs `bash ci.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
