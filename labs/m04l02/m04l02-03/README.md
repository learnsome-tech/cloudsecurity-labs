# m04l02-03 · The checks, written out in Python

**Lesson:** [Kubernetes Pod Security Standards: Baseline & Restricted](https://learnsome.tech/learn/cloudsecurity-course/m04l02) (lesson 4.2, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Read along

## Goal

You can label a namespace for Pod Security Admission, predict which pods Baseline and Restricted will reject, and roll enforcement out without breaking workloads.

In the lesson: To see exactly what the levels test, here are a few lines of Python applying six of the real checks, using the same check names the admission controller prints. First the pod level checks: any host namespace, and any host path volume. Then, for each container, a merged security context, because run as non root and the seccomp profile can be set once for the pod and overridden per container. Privileged is a Baseline check. The four Restricted checks follow: allow privilege escalation must be false, the capabilities must drop all, run as non root must be true, and the seccomp profile must be RuntimeDefault or Localhost. The real controller has more, including volume types, run as user zero, sysctls and AppArmor, but these four are the ones almost every ordinary pod trips.

## Files

- [`starter/pss.py`](starter/pss.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/pss.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–8: pod level checks
   - Lines 9–11: merged security context
   - Lines 12–22: four Restricted checks
3. Notes from the lesson:
   - Line 10: Container securityContext overrides the pod's
   - Line 16: Names match what the admission controller reports

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
