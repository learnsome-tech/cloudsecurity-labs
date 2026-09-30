# m05l04-05 · Finding the secrets in a state file

**Lesson:** [Continuous IaC Drift Detection & State Protection](https://learnsome.tech/learn/cloudsecurity-course/m05l04) (lesson 5.4, module 5: Infrastructure as Code & Policy-as-Code) · Pro  
**Check:** Graded

## Goal

You can detect drift between Terraform state and live cloud resources, handle plan exit codes correctly in a scheduled job, find secrets stored in state, and harden a remote state backend.

In the lesson: Here is a check you can run against any state file you are allowed to read. First, it prints the lineage, a unique I D fixed when the state is created, and the serial, which goes up with every write; Terraform uses both to refuse a stale or unrelated state. Then it walks each resource instance's sensitive attributes list, which Terraform records as paths, and counts the plain text characters behind each one. Last, it checks every output for any of those secret values. Run it now. The database password is marked sensitive, and it is right there. The password output is marked sensitive too. The connection string output was built from a variable nobody marked sensitive, so it carries the same password with no protection at all, and it prints in every apply log.

## Files

- [`starter/state_secrets.py`](starter/state_secrets.py): the listing from the lesson
- [`starter/terraform.tfstate`](starter/terraform.tfstate)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-05/starter`
2. Read `state_secrets.py` the way the lesson builds it:
   - Lines 1–4: it prints the lineage
   - Lines 5–13: walks each resource instance's sensitive attributes
   - Lines 14–17: it checks every output
3. Run it: `python3 state_secrets.py`.
4. Check it from the repository root: `./check m05l04-05`.

## Expected output

```text
lineage 3f2c9a1e-8b7d-4c6a-9e15-2d4b7a0c1f88, serial 42
aws_db_instance.payroll.password: marked sensitive, 30 characters in plain text
output db_password: marked sensitive, contains a secret: True
output db_url: not marked, contains a secret: True
```

## How to check

`./check m05l04-05` copies `starter/` into a scratch directory and runs `python3 state_secrets.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
