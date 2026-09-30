# m05l03-08 · The revised plan, and the violation that stays

**Lesson:** [Enforcing OPA Guardrails on Terraform Plan Payloads](https://learnsome.tech/learn/cloudsecurity-course/m05l03) (lesson 5.3, module 5: Infrastructure as Code & Policy-as-Code) · Pro  
**Check:** Graded

## Goal

You can read a Terraform plan's JSON, map data types and classifications to protection methods, and write plan guardrails that enforce classification, encryption at rest and safe replacements.

In the lesson: The team revised the change. The volume is now encrypted, the queue is labelled internal, and instead of flipping the flag on the live database, a new instance, payroll v two, is restored from an encrypted snapshot copy, with the old one left alone. The script first lists the changes in the revised plan with their actions, and then we run the guard on the revised plan. One violation remains, and it is correct: the old payroll database still exists, still unencrypted, as a no op entry. Policy on a plan judges the whole planned state, not only the diff. So you have a choice to make. Either keep that strictness and grant a recorded, time limited exception for the migration, or scope the rule to resources that are changing and leave existing debt to posture management, which module six covers.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/guard.py`](starter/guard.py)
- [`starter/plan-fixed.json`](starter/plan-fixed.json)
- [`starter/revised.sh`](starter/revised.sh): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-08/starter`
2. Read `revised.sh` the way the lesson builds it:
   - Lines 1–3: lists the changes in the revised plan
   - Lines 4–5: run the guard on the revised plan
3. Run it: `bash revised.sh`.
4. Check it from the repository root: `./check m05l03-08`.

## Expected output

```text
no-op  aws_db_instance.payroll
create  aws_db_instance.payroll_v2
create  aws_ebs_volume.scratch
create  aws_sqs_queue.events
update  aws_s3_bucket.site_assets
aws_db_instance.payroll: sensitive data not encrypted at rest
1 violation(s) in 5 changes
exit code 1
```

## How to check

`./check m05l03-08` copies `starter/` into a scratch directory and runs `bash revised.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
