# m06l03 · Envelope Encryption & Data Protection with KMS

Module 6: Cloud Detection, Encryption & Compliance · lesson 6.3 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m06l03)

**Goal:** You can explain and carry out envelope encryption, work out whether a principal may use a KMS key from its key policy and IAM policies, and choose rotation, encryption context and deletion settings knowing what each one protects against.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l03-02](m06l03-02/) | Sealing a payroll file in an envelope | Graded |
| [m06l03-03](m06l03-03/) | Opening the envelope, and failing to | Graded |
| [m06l03-05](m06l03-05/) | A key policy that separates admins from users | Read along |
| [m06l03-06](m06l03-06/) | The authorisation rule, written as code | Read along |
| [m06l03-07](m06l03-07/) | Five requests against the key policy | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Break the envelope and the policy

1. In decrypt.sh, flip one byte of data-key.enc before unwrapping; predict the output first
2. Add a Deny statement to key-policy.json for kms:PutKeyPolicy by platform-admin; rerun
3. Add a request to check.py: payroll-app with no context at all. Allowed or not?
4. Change the key policy root statement to kms:*; which check.py lines change?

> **Hint:** printf '\x00' | dd of=data-key.enc bs=1 seek=5 conv=notrunc overwrites one byte.

## Check yourself

- Why does KMS return the data key twice, and what would go wrong if you stored the plaintext copy next to the file?
- An administrator's IAM policy allows kms:* yet Decrypt on a key is refused. Which key policy statement explains that?
- The payroll role decrypts with the context department=hr and is refused. Which two mechanisms could cause that refusal?
- Why is kms:PutKeyPolicy for an administrator effectively a path to Decrypt, and how would you detect its use?
- Automatic rotation has been on for three years. Can data encrypted in the first year still be decrypted, and why?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
