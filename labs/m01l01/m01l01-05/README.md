# m01l01-05 · Which admin ports can the internet reach?

**Lesson:** [Shared Responsibility Model & Cloud Threat Landscapes](https://learnsome.tech/learn/cloudsecurity-course/m01l01) (lesson 1.1, module 1: Multi-Account Cloud Architecture & Isolation) · Free  
**Check:** Graded

## Goal

You can say which security tasks stay with you in each cloud service model, audit a real security group export for admin ports open to the internet, and check bucket regions against a data residency rule.

In the lesson: Here is a short audit that reads that file and asks one question: which admin ports can be reached from outside private address space? The admin table maps the ports we care about to names. The internal list holds the private ranges from R F C nineteen eighteen plus the I P version six unique local range, and the internal function uses real subnet maths, so a slash one is judged by what it contains rather than how it looks. The ports function treats protocol minus one as every admin port, ignores protocols other than T C P, and otherwise checks the port range. The loop then walks every range of every rule. Three groups come back. Bastion exposes SSH to every I P version four address. Legacy admin exposes everything over I P version six, which audits often forget. Ops tools exposes MySQL and R D P through a port range somebody widened. Web and the database are absent, as they should be.

## Files

- [`starter/audit_sg.py`](starter/audit_sg.py): the listing from the lesson
- [`starter/sg.json`](starter/sg.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-05/starter`
2. Read `audit_sg.py` the way the lesson builds it:
   - Lines 1–6: the admin table
   - Lines 7–9: the internal function
   - Lines 10–13: the ports function
   - Lines 14–22: the loop then
3. Run it: `python3 audit_sg.py`.
4. Check it from the repository root: `./check m01l01-05`.

## Expected output

```text
bastion       0.0.0.0/0  reaches ssh
legacy-admin  ::/0       reaches ssh, mysql, rdp, postgres
ops-tools     0.0.0.0/1  reaches mysql, rdp
```

## How to check

`./check m01l01-05` copies `starter/` into a scratch directory and runs `python3 audit_sg.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
