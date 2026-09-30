# m06l01-03 · Signing an hour of log files, the way CloudTrail does

**Lesson:** [CloudTrail Logging, Integrity Validation & Athena](https://learnsome.tech/learn/cloudsecurity-course/m06l01) (lesson 6.1, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Graded

## Goal

You can design a CloudTrail trail whose logs survive an intruder, prove with signed digests whether a log file was altered, query the archive with Athena, and write and read a Kubernetes API server audit policy.

In the lesson: Log file validation is a setting on the trail. The console turns it on for new trails; the A P I and the command line leave it off unless you ask. Once it is on, CloudTrail writes a digest file every hour into its own folder. The digest lists every log file delivered in that hour with its S H A two five six hash, and CloudTrail signs the digest with an R S A private key that only it holds. This script does the same to our two log files, so you can watch the mechanism. The sha two five six helper hashes a file's bytes. Sign digest lists each log file with its hash and the end of the hour. Then openssl makes a key pair, standing in for CloudTrail's key, and signs the digest. Run it and you get one hash per log file.

## Files

- [`starter/digest.py`](starter/digest.py): the listing from the lesson
- [`starter/logs/111122223333_CloudTrail_eu-west-2_20260927T0905Z_7Qm2.json`](starter/logs/111122223333_CloudTrail_eu-west-2_20260927T0905Z_7Qm2.json)
- [`starter/logs/111122223333_CloudTrail_eu-west-2_20260927T0915Z_Kx9d.json`](starter/logs/111122223333_CloudTrail_eu-west-2_20260927T0915Z_Kx9d.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-03/starter`
2. Read `digest.py` the way the lesson builds it:
   - Lines 1–7: the sha two five six helper
   - Lines 8–13: sign digest lists each log file
   - Lines 14–18: then openssl makes a key pair
   - Lines 19–22: run it
3. Notes from the lesson:
   - Line 11: Real digests also carry the previous digest's signature
4. Run it: `python3 digest.py`.
5. Check it from the repository root: `./check m06l01-03`.

## Expected output

```text
20260927T0905Z_7Qm2.json da98ded047b2a94e3f6717fe83e1a03a
20260927T0915Z_Kx9d.json 732ce50a397b49c96dfe5728626ff8f8
```

## How to check

`./check m06l01-03` copies `starter/` into a scratch directory and runs `python3 digest.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
