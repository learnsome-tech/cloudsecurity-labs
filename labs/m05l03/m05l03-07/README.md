# m05l03-07 · The guardrails against the plan

**Lesson:** [Enforcing OPA Guardrails on Terraform Plan Payloads](https://learnsome.tech/learn/cloudsecurity-course/m05l03) (lesson 5.3, module 5: Infrastructure as Code & Policy-as-Code) · Pro  
**Check:** Graded

## Goal

You can read a Terraform plan's JSON, map data types and classifications to protection methods, and write plan guardrails that enforce classification, encryption at rest and safe replacements.

In the lesson: OPA is not installed here, so this is a Python mirror of those three rules, not the engine. It walks the resource changes, reads the classification from after and the old classification from before, and yields a message for each rule that fires. A set removes duplicates, just as a Rego set would, and the exit code is non zero when anything is denied, which is what fails the pipeline. Now run it on the plan. Three violations, one per rule: the payroll replacement destroys restricted data, the scratch volume holds confidential data unencrypted, and the events queue has no label. Notice that the payroll change was an attempt to add encryption. The guardrail does not judge intent; it judges what the plan will do.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/guard.py`](starter/guard.py): the listing from the lesson
- [`starter/plan.json`](starter/plan.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-07/starter`
2. Read `guard.py` the way the lesson builds it:
   - Lines 1–8: it walks the resource changes
   - Lines 9–15: yields a message for each rule that fires
   - Lines 16–22: a set removes duplicates
3. Run it: `python3 guard.py plan.json`.
4. Check it from the repository root: `./check m05l03-07`.

## Expected output

```text
aws_db_instance.payroll: plan destroys restricted data
aws_ebs_volume.scratch: sensitive data not encrypted at rest
aws_sqs_queue.events: no data_classification tag
3 violation(s) in 4 changes
```

## How to check

`./check m05l03-07` copies `starter/` into a scratch directory and runs `python3 guard.py plan.json` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
