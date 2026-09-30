# m04l02-06 · Pre-flight: what breaks if we enforce Restricted?

**Lesson:** [Kubernetes Pod Security Standards: Baseline & Restricted](https://learnsome.tech/learn/cloudsecurity-course/m04l02) (lesson 4.2, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Graded

## Goal

You can label a namespace for Pod Security Admission, predict which pods Baseline and Restricted will reject, and roll enforcement out without breaking workloads.

In the lesson: Before flipping enforce to restricted, find out what would break. The input is the output of kubectl get pods dash n shop dash o json, saved to a file. We evaluate every running pod at both levels and count violations, then tally by check. Two web replicas and the orders worker only need security context changes, the kind of fix a team can ship in a day. The node exporter is different. It fails Baseline because it genuinely needs the host's network and process namespaces and the node's root filesystem to do its job. Changing its spec would break it. The cluster can give you a similar answer itself: labelling the namespace with a server side dry run returns a warning for each existing pod that would violate the new level.

## Files

- [`starter/pods.json`](starter/pods.json)
- [`starter/preflight.py`](starter/preflight.py): the listing from the lesson
- [`starter/pss.py`](starter/pss.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-06/starter`
2. Read `preflight.py` the way the lesson builds it:
   - Lines 1–6: kubectl get pods
   - Lines 7–13: every running pod
   - Lines 14–16: tally by check
3. Run it: `python3 preflight.py`.
4. Check it from the repository root: `./check m04l02-06`.

## Expected output

```text
web-7d9c6b5f4-x2kqp      baseline 0   restricted 4
web-7d9c6b5f4-m8vzt      baseline 0   restricted 4
orders-worker-0          baseline 0   restricted 2
node-exporter-9fz4d      baseline 3   restricted 6
checks to fix before enforce=restricted:
  4 x unrestricted capabilities
  4 x seccompProfile
  3 x allowPrivilegeEscalation != false
  2 x runAsNonRoot != true
  2 x host namespaces
  1 x hostPath volumes
```

## How to check

`./check m04l02-06` copies `starter/` into a scratch directory and runs `python3 preflight.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
