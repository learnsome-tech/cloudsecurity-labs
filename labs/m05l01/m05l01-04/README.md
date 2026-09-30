# m05l01-04 · The exit code is the gate

**Lesson:** [Static IaC Scanning: Linting Terraform with Checkov](https://learnsome.tech/learn/cloudsecurity-course/m05l01) (lesson 5.1, module 5: Infrastructure as Code & Policy-as-Code) · Pro  
**Check:** Graded

## Goal

You can read Checkov findings on a Terraform file, explain the logic behind a check such as CKV_AWS_24, wire the scan's exit code into a pipeline gate, and add a custom YAML check.

In the lesson: In a pipeline, a finding only matters through the exit code. This script is what a C I step does: scan, keep the code, and let the runner decide. It scans the original file and then a fixed copy. The fixed file makes two changes. The bastion group has no ingress rule at all, because engineers now reach the instance through Systems Manager Session Manager, which needs no inbound port. The admin rule's source is narrowed to the office range. The first scan exits with one, and a C I runner treats any non zero exit as a failed step, so the merge is blocked. The second exits with zero. Checkov behaves the same way, unless someone adds its soft fail flag, which forces a zero exit and quietly turns the gate into a report nobody reads.

## Files

- [`starter/check_sg.py`](starter/check_sg.py)
- [`starter/command.txt`](starter/command.txt)
- [`starter/gate.sh`](starter/gate.sh): the listing from the lesson
- [`starter/network-fixed.tf.json`](starter/network-fixed.tf.json)
- [`starter/network.tf.json`](starter/network.tf.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-04/starter`
2. Read `gate.sh` the way the lesson builds it:
   - Lines 1: scan, keep the code, and let the runner decide
   - Lines 2–6: the fixed file makes two changes
3. Run it: `bash gate.sh`.
4. Check it from the repository root: `./check m05l01-04`.

## Expected output

```text
scanning network.tf.json
CKV_AWS_24 FAILED aws_security_group.bastion
  SSH for the on-call engineer: ports 22-22
CKV_AWS_24 FAILED aws_security_group.admin
  admin tools, all TCP: ports 0-65535
CKV_AWS_24 PASSED aws_security_group.office
CKV_AWS_24 PASSED aws_security_group.web
exit code 1
scanning network-fixed.tf.json
CKV_AWS_24 PASSED aws_security_group.bastion
CKV_AWS_24 PASSED aws_security_group.admin
CKV_AWS_24 PASSED aws_security_group.office
CKV_AWS_24 PASSED aws_security_group.web
exit code 0
```

## How to check

`./check m05l01-04` copies `starter/` into a scratch directory and runs `bash gate.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
