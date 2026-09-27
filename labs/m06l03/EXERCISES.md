# Exercises — Envelope Encryption & Data Protection with KMS

Lesson `m06l03` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m06l03)

## Exercise 1: Break the envelope and the policy

1. In decrypt.sh, flip one byte of data-key.enc before unwrapping; predict the output first
2. Add a Deny statement to key-policy.json for kms:PutKeyPolicy by platform-admin; rerun
3. Add a request to check.py: payroll-app with no context at all. Allowed or not?
4. Change the key policy root statement to kms:*; which check.py lines change?

> **Hint**: printf '\x00' | dd of=data-key.enc bs=1 seek=5 conv=notrunc overwrites one byte.


---

© LearnSome.tech · support@iwantto.learnsome.tech
