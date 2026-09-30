# m02l05-06 · Offboarding through SCIM, mid-session

**Lesson:** [Zero-Trust Network Access & IdP Federation](https://learnsome.tech/learn/cloudsecurity-course/m02l05) (lesson 2.5, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Graded

## Goal

You can explain how a zero-trust broker decides each request from identity, group and device, and deprovision a user through SCIM so access ends mid-session.

In the lesson: Now a leaver. Alice's request works before anything happens. Then the identity provider sends the S C I M patch it sends when H R marks someone as gone: the patch operation schema, and one operation replacing active with false, addressed to her S C I M I D. The broker answers two oh four, no content. On her very next request, with a token that is still valid for forty three minutes, Alice is refused, because the broker consults the directory on every request. A V P N tunnel she opened this morning would still be up. For apps that only check the token, the OpenID Foundation's continuous access evaluation profile defines events such as session revoked, so a provider can tell them to end a session straight away.

## Files

- [`starter/broker.py`](starter/broker.py)
- [`starter/devices.json`](starter/devices.json)
- [`starter/directory.json`](starter/directory.json)
- [`starter/harness.py`](starter/harness.py)
- [`starter/idp.py`](starter/idp.py)
- [`starter/offboard.py`](starter/offboard.py): the listing from the lesson
- [`starter/server.py`](starter/server.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-06/starter`
2. Read `offboard.py` the way the lesson builds it:
   - Lines 1–8: works before anything happens
   - Lines 9–16: the identity provider sends the S C I M patch
   - Lines 17–20: on her very next request
3. Run it: `python3 offboard.py`.
4. Check it from the repository root: `./check m02l05-06`.

## Expected output

```text
before: 200 payroll for alice@example.com
SCIM PATCH: 204
after:  403 account is disabled in the directory
alice's token is still valid for 43 minutes
```

## How to check

`./check m02l05-06` copies `starter/` into a scratch directory and runs `python3 offboard.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
