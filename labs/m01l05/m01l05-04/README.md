# m01l05-04 · Overlapping ranges: who can never peer

**Lesson:** [Cloud Network Isolation: VPC Peering & PrivateLink](https://learnsome.tech/learn/cloudsecurity-course/m01l05) (lesson 1.5, module 1: Multi-Account Cloud Architecture & Isolation) · Free  
**Check:** Graded

## Goal

You can trace a packet through peered VPC route tables, spot CIDR overlaps that block peering, and choose between peering and PrivateLink by what each one exposes.

In the lesson: Before any of that, the ranges must not overlap. This reads describe V P Cs output for six V P Cs and keeps every associated block, primary and secondary, because a secondary block counts too. It then compares every pair with the overlaps method. Four pairs come back. The M L sandbox was built from a template that always uses ten dot zero slash sixteen, so it collides with the data lake. Shared services looks clean until you notice its secondary block sits inside payments dev. And the vendor's scanner, in an account we do not own, overlaps both ten dot zero V P Cs. Renumbering a live V P C is painful, and you cannot renumber a vendor. This is where PrivateLink comes in.

## Files

- [`starter/overlap.py`](starter/overlap.py): the listing from the lesson
- [`starter/vpcs.json`](starter/vpcs.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-04/starter`
2. Read `overlap.py` the way the lesson builds it:
   - Lines 1–10: every associated block
   - Lines 11–15: compares every pair
3. Run it: `python3 overlap.py`.
4. Check it from the repository root: `./check m01l05-04`.

## Expected output

```text
cannot peer payments-dev with shared-services: 10.21.0.0/16 and 10.21.64.0/18
cannot peer data-lake with ml-sandbox: 10.0.0.0/16 and 10.0.0.0/16
cannot peer data-lake with vendor-scanner: 10.0.0.0/16 and 10.0.128.0/20
cannot peer ml-sandbox with vendor-scanner: 10.0.0.0/16 and 10.0.128.0/20
```

## How to check

`./check m01l05-04` copies `starter/` into a scratch directory and runs `python3 overlap.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
