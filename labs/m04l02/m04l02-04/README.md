# m04l02-04 · An ordinary pod against both levels

**Lesson:** [Kubernetes Pod Security Standards: Baseline & Restricted](https://learnsome.tech/learn/cloudsecurity-course/m04l02) (lesson 4.2, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Graded

## Goal

You can label a namespace for Pod Security Admission, predict which pods Baseline and Restricted will reject, and roll enforcement out without breaking workloads.

In the lesson: We run three pods through both levels and stop at the first level that forbids them, since Restricted includes every Baseline check. The web pod is what most teams write: an image and a port, no security context at all. It passes Baseline, because it asks for nothing dangerous. It fails Restricted four times, because Restricted wants you to say out loud that you are not root, cannot escalate, hold no capabilities and are filtered by seccomp. The hardened pod passes both. The log agent fails Baseline on host P I D, a host path mount of var log, and privileged mode. That is the difference in one screen: Baseline catches pods that ask for the node, Restricted catches pods that merely fail to lock themselves down.

## Files

- [`starter/admit.py`](starter/admit.py): the listing from the lesson
- [`starter/hardened-pod.json`](starter/hardened-pod.json)
- [`starter/log-agent.json`](starter/log-agent.json)
- [`starter/pss.py`](starter/pss.py)
- [`starter/web-pod.json`](starter/web-pod.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-04/starter`
2. Read `admit.py` the way the lesson builds it:
   - Lines 1–4: three pods
   - Lines 5–12: stop at the first level
3. Run it: `python3 admit.py`.
4. Check it from the repository root: `./check m04l02-04`.

## Expected output

```text
web-pod.json at baseline: allowed
web-pod.json at restricted: forbidden
  allowPrivilegeEscalation != false (container "app")
  unrestricted capabilities (container "app")
  runAsNonRoot != true (container "app")
  seccompProfile (container "app")
hardened-pod.json at baseline: allowed
hardened-pod.json at restricted: allowed
log-agent.json at baseline: forbidden
  host namespaces (hostPID=true)
  hostPath volumes (volume "varlog")
  privileged (container "agent")
```

## How to check

`./check m04l02-04` copies `starter/` into a scratch directory and runs `python3 admit.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
