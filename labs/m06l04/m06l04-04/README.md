# m06l04-04 · Evaluating six resources

**Lesson:** [Cloud Security Posture Management & Remediation](https://learnsome.tech/learn/cloudsecurity-course/m06l04) (lesson 6.4, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Graded

## Goal

You can write posture controls against real AWS Config configuration items, decide which failures to fix automatically and which to hand to a person, and build remediation with exceptions, ownership and a blast radius limit.

In the lesson: Run the controls over six configuration items. The bastion group has S S H open to the world. The web load balancer allows four hundred and forty three from everywhere, which is its job, so it passes. Debug temp is the interesting one: an all traffic rule from every I P version six address, so both admin ports are open although nobody typed twenty two anywhere. Vendor R D P passes, because its range is one vendor network, not the internet. Both buckets have public policies unblocked. Six resources and four failures, and nothing here says which to fix first. That needs context the configuration item does not have: who owns it, what data it holds, and whether a fix is already agreed.

## Files

- [`starter/config-items.json`](starter/config-items.json)
- [`starter/controls.py`](starter/controls.py)
- [`starter/evaluate.py`](starter/evaluate.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l04/m06l04-04/starter`
2. Read `evaluate.py` the way the lesson builds it:
   - Lines 1–7: run the controls
3. Run it: `python3 evaluate.py`.
4. Check it from the repository root: `./check m06l04-04`.

## Expected output

```text
NON_COMPLIANT bastion-ssh
  port 22 open to 0.0.0.0/0
COMPLIANT web-alb
NON_COMPLIANT debug-temp
  port 22 open to ::/0
  port 3389 open to ::/0
COMPLIANT vendor-rdp
NON_COMPLIANT example-payroll-exports
  blockPublicPolicy is off
  restrictPublicBuckets is off
NON_COMPLIANT example-marketing-site
  blockPublicPolicy is off
  restrictPublicBuckets is off
```

## How to check

`./check m06l04-04` copies `starter/` into a scratch directory and runs `python3 evaluate.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
