# m05l04-06 · backend.tf: an encrypted, locked, versioned home

**Lesson:** [Continuous IaC Drift Detection & State Protection](https://learnsome.tech/learn/cloudsecurity-course/m05l04) (lesson 5.4, module 5: Infrastructure as Code & Policy-as-Code) · Pro  
**Check:** Checker

## Goal

You can detect drift between Terraform state and live cloud resources, handle plan exit codes correctly in a scheduled job, find secrets stored in state, and harden a remote state backend.

In the lesson: Protection starts with the backend. This S three backend stores state in a dedicated bucket, with encrypt set so the object is encrypted at rest, and a customer managed K M S key, so reading state needs both S three read and K M S decrypt permission. Next, use lockfile turns on locking with a lock object in the same bucket, which recent Terraform versions support; older setups use a DynamoDB table. Locking stops two applies writing at once and corrupting state. Finally, the comments list what the bucket itself needs: versioning to roll back a bad write, public access blocked, a bucket policy that refuses requests without T L S, and a key policy that lets only the deploy and drift roles decrypt. Keep production state in its own account, away from developer credentials.

## Files

- [`starter/backend.tf`](starter/backend.tf): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-06/starter`
2. Read `backend.tf` the way the lesson builds it:
   - Lines 1–7: this S three backend stores state
   - Lines 8–10: use lockfile turns on locking
   - Lines 11–16: the comments list what the bucket itself needs
3. Edit `backend.tf` and check it: `terraform init; terraform validate`.
4. Check it from the repository root: `./check m05l04-06`.

## How to check

`./check m05l04-06` copies `starter/` into a scratch directory and runs `terraform init; terraform validate` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it initialises the configuration (the local, null and random providers) and runs `terraform validate`: it passes when the configuration is valid. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
