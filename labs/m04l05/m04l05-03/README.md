# m04l05-03 · Auditing the flags like a benchmark would

**Lesson:** [Securing the Kubernetes Control Plane & Node Components](https://learnsome.tech/learn/cloudsecurity-course/m04l05) (lesson 4.5, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Graded

## Goal

You can audit API server and kubelet settings against CIS-style checks, and turn on and verify encryption at rest for Secrets in etcd.

In the lesson: This script pulls every flag out of the manifest with one regular expression, the same way you would grep for it on the node. Then eight checks, modelled on the kind of test the C I S Kubernetes Benchmark describes and kube bench automates. Two details matter. Anonymous auth has to be explicitly false, because when the flag is absent the built in default is true. Profiling is the same. Each check prints pass or fail. Three pass: the authorisation modes and NodeRestriction. Five of eight fail. Anonymous requests are accepted, so anyone who can reach port six four four three can call endpoints that grant the anonymous user access. There is no audit trail of who did what, Secrets reach etcd unencrypted, and the A P I server does not verify which kubelet it is talking to when it opens exec sessions.

## Files

- [`starter/audit_flags.py`](starter/audit_flags.py): the listing from the lesson
- [`starter/kube-apiserver.yaml`](starter/kube-apiserver.yaml)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-03/starter`
2. Read `audit_flags.py` the way the lesson builds it:
   - Lines 1–5: every flag
   - Lines 6–16: eight checks
   - Lines 17–19: pass or fail
3. Notes from the lesson:
   - Line 7: Absent flag: the built-in default applies
4. Run it: `python3 audit_flags.py`.
5. Check it from the repository root: `./check m04l05-03`.

## Expected output

```text
fail anonymous-auth=false
pass authorization-mode has Node and RBAC
pass authorization-mode has no AlwaysAllow
pass NodeRestriction admission plugin
fail profiling=false
fail audit-log-path set
fail encryption-provider-config set
fail kubelet CA set
5 of 8 checks fail
```

## How to check

`./check m04l05-03` copies `starter/` into a scratch directory and runs `python3 audit_flags.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
