# m06l03-03 · Opening the envelope, and failing to

**Lesson:** [Envelope Encryption & Data Protection with KMS](https://learnsome.tech/learn/cloudsecurity-course/m06l03) (lesson 6.3, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Graded

## Goal

You can explain and carry out envelope encryption, work out whether a principal may use a KMS key from its key policy and IAM policies, and choose rotation, encryption context and deletion settings knowing what each one protects against.

In the lesson: Decryption runs the other way, and only the forty byte encrypted key travels to K M S. The unwrap function is what the Decrypt call does inside the hardware: take the encrypted data key, unwrap it with the K M S key, and hand back plaintext. With the right key, the payroll rows come back. With a different key, even one of the right size and type, the key wrap's integrity check refuses, so a wrong key never produces convincing garbage. Last, delete the key. Every copy of that file, in every backup and every replica, is now permanently unreadable. That is crypto shredding, and it is the most reliable way to destroy data you cannot find all the copies of.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/decrypt.sh`](starter/decrypt.sh): the listing from the lesson
- [`starter/envelope.sh`](starter/envelope.sh)
- [`starter/payroll.csv`](starter/payroll.csv)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-03/starter`
2. Read `decrypt.sh` the way the lesson builds it:
   - Lines 1–7: the unwrap function
   - Lines 8–13: with the right key
   - Lines 14–17: a different key
   - Lines 18–21: delete the key
3. Run it: `bash decrypt.sh`.
4. Check it from the repository root: `./check m06l03-03`.

## Expected output

```text
employee_id,name
E1001,Ada Example
E1002,Ben Sample
E1003,Cara Placeholder
other key: unwrap refused, integrity check failed
key deleted: nothing can unwrap it
```

## How to check

`./check m06l03-03` copies `starter/` into a scratch directory and runs `bash decrypt.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
