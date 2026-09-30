# m05l01-03 · The logic behind CKV_AWS_24, applied to four groups

**Lesson:** [Static IaC Scanning: Linting Terraform with Checkov](https://learnsome.tech/learn/cloudsecurity-course/m05l01) (lesson 5.1, module 5: Infrastructure as Code & Policy-as-Code) · Pro  
**Check:** Graded

## Goal

You can read Checkov findings on a Terraform file, explain the logic behind a check such as CKV_AWS_24, wire the scan's exit code into a pipeline gate, and add a custom YAML check.

In the lesson: Checkov isn't installed on this machine, so rather than fake its output, here are a few lines of Python that ask the same question as check twenty four, against real Terraform. Terraform accepts JSON syntax as well as H C L, in files ending dot T F dot JSON, and Python reads those without a special parser. The function exposes ssh answers two questions. First, does the rule's port range include twenty two, remembering that protocol minus one means every port? Second, is any source network a prefix of length zero, which covers anywhere in both I P version four and version six? The loop then reports each security group as passed or failed, and the program exits with one if anything failed. Now run it against four groups, and watch the admin group: it never mentions port twenty two, yet it fails.

## Files

- [`starter/check_sg.py`](starter/check_sg.py): the listing from the lesson
- [`starter/command.txt`](starter/command.txt)
- [`starter/network.tf.json`](starter/network.tf.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-03/starter`
2. Read `check_sg.py` the way the lesson builds it:
   - Lines 1–10: the function exposes ssh answers two questions
   - Lines 11–20: the loop then reports each security group
3. Notes from the lesson:
   - Line 4: a range such as 0-65535 contains 22 as well
   - Line 8: 0.0.0.0/0 and ::/0 both have prefix length 0
4. Run it: `python3 check_sg.py network.tf.json`.
5. Check it from the repository root: `./check m05l01-03`.

## Expected output

```text
CKV_AWS_24 FAILED aws_security_group.bastion
  SSH for the on-call engineer: ports 22-22
CKV_AWS_24 FAILED aws_security_group.admin
  admin tools, all TCP: ports 0-65535
CKV_AWS_24 PASSED aws_security_group.office
CKV_AWS_24 PASSED aws_security_group.web
```

## How to check

`./check m05l01-03` copies `starter/` into a scratch directory and runs `python3 check_sg.py network.tf.json` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
