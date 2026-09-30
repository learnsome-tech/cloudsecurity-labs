# m02l05-05 · Five requests, five decisions

**Lesson:** [Zero-Trust Network Access & IdP Federation](https://learnsome.tech/learn/cloudsecurity-course/m02l05) (lesson 2.5, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Graded

## Goal

You can explain how a zero-trust broker decides each request from identity, group and device, and deprovision a user through SCIM so access ends mid-session.

In the lesson: This program starts the broker on the loopback address, on a port the operating system picks, and signs tokens for Alice, who is in payroll admins, and Bob, who is in engineering. Then Bob tries something: he decodes his own token, changes his group to payroll admins, and keeps the old signature. Five requests follow. Alice on her company laptop gets in. Alice on her personal tablet is refused because the tablet is not managed, even though her identity is perfect. Bob on his company laptop is refused, since none of his groups grants payroll. Bob's edited token fails the signature check and is told to sign in again, and no token at all gets the same four oh one. Every answer names its reason, which is exactly what you want in the broker's logs.

## Files

- [`starter/broker.py`](starter/broker.py)
- [`starter/devices.json`](starter/devices.json)
- [`starter/directory.json`](starter/directory.json)
- [`starter/harness.py`](starter/harness.py)
- [`starter/idp.py`](starter/idp.py)
- [`starter/server.py`](starter/server.py)
- [`starter/try_access.py`](starter/try_access.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-05/starter`
2. Read `try_access.py` the way the lesson builds it:
   - Lines 1–6: starts the broker
   - Lines 7–9: then bob tries something
   - Lines 10–18: five requests follow
3. Run it: `python3 try_access.py`.
4. Check it from the repository root: `./check m02l05-05`.

## Expected output

```text
alice, company laptop   200 payroll for alice@example.com
alice, personal tablet  403 device fails posture: managed
bob, company laptop     403 no group of yours grants this app
bob, edited groups      401 sign in again: bad signature
no token                401 sign in again: no token
```

## How to check

`./check m02l05-05` copies `starter/` into a scratch directory and runs `python3 try_access.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
