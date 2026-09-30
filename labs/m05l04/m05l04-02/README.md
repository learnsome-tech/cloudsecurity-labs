# m05l04-02 · What a refresh compares: state against the cloud

**Lesson:** [Continuous IaC Drift Detection & State Protection](https://learnsome.tech/learn/cloudsecurity-course/m05l04) (lesson 5.4, module 5: Infrastructure as Code & Policy-as-Code) · Pro  
**Check:** Graded

## Goal

You can detect drift between Terraform state and live cloud resources, handle plan exit codes correctly in a scheduled job, find secrets stored in state, and harden a remote state backend.

In the lesson: Terraform does this comparison for you, but it helps to see exactly what is compared. This script reads the rules recorded in the state file, and the same group as the cloud describes it, in the JSON the A W S command line returns from describe security groups. Each side becomes a set of rules: protocol, from port, to port and source range. The set differences are the drift. Anything in the cloud but not in state was added outside Terraform, and anything in state but gone from the cloud was removed. The script exits with two when it finds drift, the same code terraform plan uses. Now run it against the live description. The port twenty two rule from anywhere appears with a plus sign, against the address aws security group dot web.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/describe-security-groups.json`](starter/describe-security-groups.json)
- [`starter/drift.py`](starter/drift.py): the listing from the lesson
- [`starter/terraform.tfstate`](starter/terraform.tfstate)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-02/starter`
2. Read `drift.py` the way the lesson builds it:
   - Lines 1–5: reads the rules recorded in the state file
   - Lines 6–15: each side becomes a set of rules
   - Lines 16–21: the set differences are the drift
3. Notes from the lesson:
   - Line 16: + in the cloud, not in state; - in state, gone from cloud
4. Run it: `python3 drift.py describe-security-groups.json`.
5. Check it from the repository root: `./check m05l04-02`.

## Expected output

```text
+ aws_security_group.web ingress ('tcp', 22, 22, '0.0.0.0/0')
state serial 42: drift
```

## How to check

`./check m05l04-02` copies `starter/` into a scratch directory and runs `python3 drift.py describe-security-groups.json` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
