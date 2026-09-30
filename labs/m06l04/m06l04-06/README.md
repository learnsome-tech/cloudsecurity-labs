# m06l04-06 · A remediation plan with guardrails

**Lesson:** [Cloud Security Posture Management & Remediation](https://learnsome.tech/learn/cloudsecurity-course/m06l04) (lesson 6.4, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Graded

## Goal

You can write posture controls against real AWS Config configuration items, decide which failures to fix automatically and which to hand to a person, and build remediation with exceptions, ownership and a blast radius limit.

In the lesson: This planner puts those rules into code. Today is fixed, so the output is repeatable, the change cap is the blast radius, and the actions table says what each fix would be. For each failing item, a current exception means skip it and say so. A group that Terraform owns becomes a ticket, because changing it by hand creates drift, and the next apply would put the open rule straight back. Everything else joins the plan, and the plan is refused if it is too big. The output is a dry run. The bastion becomes a ticket for the platform team. The marketing bucket is skipped until next March. Debug temp had an exception that ran out last week, so it is back in the plan, alongside the payroll bucket.

## Files

- [`starter/config-items.json`](starter/config-items.json)
- [`starter/controls.py`](starter/controls.py)
- [`starter/remediate.py`](starter/remediate.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l04/m06l04-06/starter`
2. Read `remediate.py` the way the lesson builds it:
   - Lines 1–7: today is fixed
   - Lines 8–13: for each failing item
   - Lines 14–19: a group that Terraform owns
   - Lines 20–22: everything else joins the plan
3. Run it: `python3 remediate.py`.
4. Check it from the repository root: `./check m06l04-06`.

## Expected output

```text
ticket bastion-ssh: Terraform owns it, fix the code
skip   example-marketing-site: exception until 2027-03-31
dry run, would:
  revoke world-open admin rules on sg-0c3d4e5f607182930
  turn on all four public access blocks for example-payroll-exports
```

## How to check

`./check m06l04-06` copies `starter/` into a scratch directory and runs `python3 remediate.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
