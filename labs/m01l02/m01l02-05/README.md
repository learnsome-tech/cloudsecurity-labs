# m01l02-05 · Placement is access: the organisation path condition

**Lesson:** [AWS Organizations, Account Hierarchies & Azure Management Groups](https://learnsome.tech/learn/cloudsecurity-course/m01l02) (lesson 1.2, module 1: Multi-Account Cloud Architecture & Isolation) · Free  
**Check:** Graded

## Goal

You can lay out an AWS organisation or Azure management group tree so each account limits blast radius, and work out which accounts an organisation path condition will let in.

In the lesson: Placement also decides access. A bucket or key policy can admit principals by the condition key a w s principal org paths, whose value is the organisation I D, the root, then every unit down to the account's parent, each followed by a slash. The org path function builds exactly that string. Policies usually compare it with string like, where a star matches any run of characters, slashes included, and a question mark matches one character. The string like function converts the pattern into a regular expression with those two wildcards and nothing else. The pattern admits anything under Workloads. Only the two payments accounts match, at any depth below that unit. Data lake prod does not, so its jobs would be refused by a bucket that trusts production. Moving an account between units changes what it can reach.

## Files

- [`starter/org.json`](starter/org.json)
- [`starter/orgpaths.py`](starter/orgpaths.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-05/starter`
2. Read `orgpaths.py` the way the lesson builds it:
   - Lines 1–12: the org path function
   - Lines 13–16: string like
   - Lines 17–21: the pattern
3. Run it: `python3 orgpaths.py`.
4. Check it from the repository root: `./check m01l02-05`.

## Expected output

```text
management        o-a1b2c3d4e5/r-a1b2/                                 False
log-archive       o-a1b2c3d4e5/r-a1b2/ou-a1b2-sec00001/                False
security-tooling  o-a1b2c3d4e5/r-a1b2/ou-a1b2-sec00001/                False
payments-prod     o-a1b2c3d4e5/r-a1b2/ou-a1b2-wkld0001/ou-a1b2-prod0001/ True
payments-dev      o-a1b2c3d4e5/r-a1b2/ou-a1b2-wkld0001/ou-a1b2-dev00001/ True
data-lake-prod    o-a1b2c3d4e5/r-a1b2/                                 False
sandbox-jo        o-a1b2c3d4e5/r-a1b2/ou-a1b2-sbox0001/                False
```

## How to check

`./check m01l02-05` copies `starter/` into a scratch directory and runs `python3 orgpaths.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
