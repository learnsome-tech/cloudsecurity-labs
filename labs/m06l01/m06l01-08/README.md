# m06l01-08 · Reading the audit log with jq

**Lesson:** [CloudTrail Logging, Integrity Validation & Athena](https://learnsome.tech/learn/cloudsecurity-course/m06l01) (lesson 6.1, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Graded

## Goal

You can design a CloudTrail trail whose logs survive an intruder, prove with signed digests whether a log file was altered, query the archive with Athena, and write and read a Kubernetes API server audit policy.

In the lesson: The file holds six audit events in the real format, one J S O N object per line, from a payments namespace. Three jq queries are what a responder runs first. Who touched secrets: the payments service account reads its database credentials twice, which is its job. Then dev sam lists secrets in payments and asks for a bootstrap token in kube system, and both come back four hundred and three. Denied requests per user groups on the authorisation decision annotation that the A P I server adds to each event. Two refusals from one person inside a minute look like someone mapping their own permissions. Shells opened inside pods filters on the exec subresource rather than the verb, because the verb depends on how the client connects. The same person who was refused secrets then opened a shell in the payments A P I pod, which runs with the service account that can read them.

## Files

- [`starter/audit-queries.sh`](starter/audit-queries.sh): the listing from the lesson
- [`starter/audit.log`](starter/audit.log)
- [`starter/command.txt`](starter/command.txt)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-08/starter`
2. Read `audit-queries.sh` the way the lesson builds it:
   - Lines 1–5: who touched secrets
   - Lines 6–9: denied requests per user
   - Lines 10–13: shells opened inside pods
3. Run it: `bash audit-queries.sh`.
4. Check it from the repository root: `./check m06l01-08`.

## Expected output

```text
who touched secrets
09:20:03 system:serviceaccount:payments:api get payments/db-credentials 200
09:22:15 dev-sam@example.com list payments/* 403
09:22:31 dev-sam@example.com get kube-system/bootstrap-token-abcdef 403
09:23:40 system:serviceaccount:payments:api get payments/db-credentials 200
denied requests per user
dev-sam@example.com 2
shells opened inside pods
dev-sam@example.com payments/api-7d9f8c6b5-x2kqp
```

## How to check

`./check m06l01-08` copies `starter/` into a scratch directory and runs `bash audit-queries.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
