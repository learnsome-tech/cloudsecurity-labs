# m04l02-05 · What a Restricted-compliant pod spec looks like

**Lesson:** [Kubernetes Pod Security Standards: Baseline & Restricted](https://learnsome.tech/learn/cloudsecurity-course/m04l02) (lesson 4.2, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Read along

## Goal

You can label a namespace for Pod Security Admission, predict which pods Baseline and Restricted will reject, and roll enforcement out without breaking workloads.

In the lesson: Here is the fix, and it is short. At pod level: run as non root true, a numeric run as user of sixty five thousand five hundred and thirty two, and a seccomp profile of type RuntimeDefault, which applies the container runtime's standard system call filter. At container level: allow privilege escalation false, which the kernel enforces as the no new privs flag, and capabilities that drop all. Those two fields exist only on containers, which is why they cannot be set once for the pod. The read only root filesystem is not part of Restricted, but it costs one line, and it removes the place a dropped payload would be written. If the app needs scratch space, mount an empty dir volume at that path instead.

## Files

- [`starter/hardened-pod.json`](starter/hardened-pod.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/hardened-pod.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–10: pod level
   - Lines 11–20: container level
3. Notes from the lesson:
   - Line 9: RuntimeDefault: the container runtime's default syscall filter
   - Line 14: Sets no_new_privs on the process
   - Line 15: Not required by Restricted, worth adding anyway

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l02-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
