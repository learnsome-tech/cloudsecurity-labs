# m06l03-07 · Five requests against the key policy

**Lesson:** [Envelope Encryption & Data Protection with KMS](https://learnsome.tech/learn/cloudsecurity-course/m06l03) (lesson 6.3, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Graded

## Goal

You can explain and carry out envelope encryption, work out whether a principal may use a KMS key from its key policy and IAM policies, and choose rotation, encryption context and deletion settings knowing what each one protects against.

In the lesson: Two roles: the payroll app, and a platform administrator whose I A M policy allows every K M S action. Five requests. Run them. The app decrypting with the payroll context is allowed by the key policy directly. The same app asking with the H R context gets an implicit deny, even though it is the same role and the same key. The administrator's decrypt is refused despite a K M S wildcard in I A M, because the key policy never passes decrypt through to I A M. Scheduling deletion and putting the key policy are both allowed. That last line is the one to remember: the administrator cannot decrypt today, and can grant themselves decrypt with one call.

## Files

- [`starter/check.py`](starter/check.py): the listing from the lesson
- [`starter/iam-policies.json`](starter/iam-policies.json)
- [`starter/key-policy.json`](starter/key-policy.json)
- [`starter/kmsauth.py`](starter/kmsauth.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-07/starter`
2. Read `check.py` the way the lesson builds it:
   - Lines 1–4: two roles
   - Lines 5–11: five requests
   - Lines 12–15: run them
3. Run it: `python3 check.py`.
4. Check it from the repository root: `./check m06l03-07`.

## Expected output

```text
payroll-app    kms:Decrypt              payroll  allow (key policy)
payroll-app    kms:Decrypt              hr       implicit deny
platform-admin kms:Decrypt              payroll  implicit deny
platform-admin kms:ScheduleKeyDeletion  -        allow (IAM, trusted by key policy)
platform-admin kms:PutKeyPolicy         -        allow (IAM, trusted by key policy)
```

## How to check

`./check m06l03-07` copies `starter/` into a scratch directory and runs `python3 check.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
