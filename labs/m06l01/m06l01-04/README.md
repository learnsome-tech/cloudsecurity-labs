# m06l01-04 · Deleting one record, then forging the digest

**Lesson:** [CloudTrail Logging, Integrity Validation & Athena](https://learnsome.tech/learn/cloudsecurity-course/m06l01) (lesson 6.1, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Graded

## Goal

You can design a CloudTrail trail whose logs survive an intruder, prove with signed digests whether a log file was altered, query the archive with Athena, and write and read a Kubernetes API server audit policy.

In the lesson: Now play the intruder. The validate function does what the validate logs command in the A W S command line does. It checks the digest's signature with the public key, then recomputes every log file hash and compares it with the digest. First, the files as delivered: signature valid, nothing changed. Next the intruder removes the stop logging record from the second file and writes it back. The signature still verifies, but that file's hash no longer matches, so validation names the changed file. A smarter intruder rewrites the digest with the new hash. The hashes now agree, and the signature fails, because the digest bytes changed and only CloudTrail holds the private key. Each real digest also carries the previous digest's signature, so deleting a whole hour breaks the chain as well. Validation proves tampering; it does not prevent it. S three Object Lock in compliance mode is what stops deletion.

## Files

- [`starter/digest.py`](starter/digest.py)
- [`starter/logs/111122223333_CloudTrail_eu-west-2_20260927T0905Z_7Qm2.json`](starter/logs/111122223333_CloudTrail_eu-west-2_20260927T0905Z_7Qm2.json)
- [`starter/logs/111122223333_CloudTrail_eu-west-2_20260927T0915Z_Kx9d.json`](starter/logs/111122223333_CloudTrail_eu-west-2_20260927T0915Z_Kx9d.json)
- [`starter/validate.py`](starter/validate.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-04/starter`
2. Read `validate.py` the way the lesson builds it:
   - Lines 1–10: the validate function
   - Lines 11–13: first, the files as delivered
   - Lines 14–18: next the intruder removes
   - Lines 19–22: a smarter intruder rewrites the digest
3. Run it: `python3 validate.py`.
4. Check it from the repository root: `./check m06l01-04`.

## Expected output

```text
as delivered: signature valid, changed []
record deleted: signature valid, changed ['Kx9d.json']
digest rewritten: signature invalid, changed []
```

## How to check

`./check m06l01-04` copies `starter/` into a scratch directory and runs `python3 validate.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
