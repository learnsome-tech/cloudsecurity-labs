# m05l03-03 · Three questions to ask any plan, answered with jq

**Lesson:** [Enforcing OPA Guardrails on Terraform Plan Payloads](https://learnsome.tech/learn/cloudsecurity-course/m05l03) (lesson 5.3, module 5: Infrastructure as Code & Policy-as-Code) · Pro  
**Check:** Graded

## Goal

You can read a Terraform plan's JSON, map data types and classifications to protection methods, and write plan guardrails that enforce classification, encryption at rest and safe replacements.

In the lesson: jq is installed, so this is the real tool on a full plan file: three questions every reviewer should ask, answered straight from the JSON. The first query prints each change's actions, address and data classification, falling back to the before state for deletions. The second finds replacements and prints the paths that forced them. The third shows what the E B S volume will not know until apply. Now run all three. Payroll is a restricted database being replaced. The events queue has no classification at all. And the volume's K M S key I D is unknown at plan time, so a rule that insists on seeing a key A R N would reject every new volume. A policy should test the encrypted flag, which is already known.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/inspect.sh`](starter/inspect.sh): the listing from the lesson
- [`starter/plan.json`](starter/plan.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-03/starter`
2. Read `inspect.sh` the way the lesson builds it:
   - Lines 1–4: the first query prints each change's actions
   - Lines 5–8: the second finds replacements
   - Lines 9–12: the third shows what the E B S volume
3. Run it: `bash inspect.sh`.
4. Check it from the repository root: `./check m05l03-03`.

## Expected output

```text
delete+create  aws_db_instance.payroll  restricted
create  aws_ebs_volume.scratch  confidential
create  aws_sqs_queue.events  none
update  aws_s3_bucket.site_assets  public
aws_db_instance.payroll replaced because of [["storage_encrypted"]]
{"arn":true,"id":true,"kms_key_id":true}
```

## How to check

`./check m05l03-03` copies `starter/` into a scratch directory and runs `bash inspect.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
