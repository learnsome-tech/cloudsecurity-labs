# m06l03-02 · Sealing a payroll file in an envelope

**Lesson:** [Envelope Encryption & Data Protection with KMS](https://learnsome.tech/learn/cloudsecurity-course/m06l03) (lesson 6.3, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Graded

## Goal

You can explain and carry out envelope encryption, work out whether a principal may use a KMS key from its key policy and IAM policies, and choose rotation, encryption context and deletion settings knowing what each one protects against.

In the lesson: Here is the same flow with openssl, so every step is visible. A random file stands in for the K M S key; in the real service you never see it. Generate data key is two steps here: a fresh random key for this one file, then that key wrapped under the K M S key with the standard A E S key wrap, which has its own integrity check. K M S itself uses A E S in G C M mode for this, and so do the A W S libraries for the data. The openssl encrypt command has no G C M mode, which is why this demo uses C B C for the file. Encrypt the payroll file with the plaintext data key, keep the initialisation vector, and delete the plaintext key. Three files remain: the encrypted payroll, a forty byte encrypted key, and nothing an attacker could decrypt without asking K M S.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/envelope.sh`](starter/envelope.sh): the listing from the lesson
- [`starter/payroll.csv`](starter/payroll.csv)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-02/starter`
2. Read `envelope.sh` the way the lesson builds it:
   - Lines 1–5: a random file stands in
   - Lines 6–10: generate data key is two steps
   - Lines 11–17: encrypt the payroll file
   - Lines 18–21: three files remain
3. Notes from the lesson:
   - Line 9: Demo only: -K puts the key on the command line, visible in ps
4. Run it: `bash envelope.sh`.
5. Check it from the repository root: `./check m06l03-02`.

## Expected output

```text
payroll.csv       191 bytes
payroll.csv.enc   192 bytes
data-key.enc       40 bytes
```

## How to check

`./check m06l03-02` copies `starter/` into a scratch directory and runs `bash envelope.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
