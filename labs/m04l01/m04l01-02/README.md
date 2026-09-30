# m04l01-02 · A two-stage Dockerfile ending in distroless

**Lesson:** [Container Hardening: Distroless & Rootless](https://learnsome.tech/learn/cloudsecurity-course/m04l01) (lesson 4.1, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Checker

## Goal

You can build a distroless, non-root image and prove from process status and ID maps what an attacker inside it can and cannot do.

In the lesson: The build stage uses a normal slim Python image, because installing dependencies needs pip and sometimes a compiler. Nothing from that stage ships except the files we copy out. Then the runtime stage starts from Google's distroless Python image with the nonroot tag. It holds the interpreter, the C library, time zone data and C A certificates, and nothing to type commands into. We set a numeric user, sixty five thousand five hundred and thirty two, which is the nonroot account distroless defines. Numeric matters: Kubernetes can only check run as non root against a number, not a name. The entrypoint uses exec form, the J S O N array. Shell form would wrap the command in bin sh dash c, and there is no bin sh here, so the container would fail to start.

## Files

- [`starter/Dockerfile`](starter/Dockerfile): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-02/starter`
2. Read `Dockerfile` the way the lesson builds it:
   - Lines 1–6: The build stage
   - Lines 7–12: the runtime stage
   - Lines 13–14: exec form
3. Notes from the lesson:
   - Line 2: Full Debian image: pip, gcc and bash stay in this stage
   - Line 9: Distroless nonroot tag: Python, libc, certificates, no shell
   - Line 13: Numeric UID so Kubernetes can verify runAsNonRoot
   - Line 14: Exec form: no bin sh needed to start the process
4. Edit `Dockerfile` and check it: `hadolint Dockerfile`.
5. Check it from the repository root: `./check m04l01-02`.

## How to check

`./check m04l01-02` copies `starter/` into a scratch directory and runs `hadolint Dockerfile` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it lints the Dockerfile with hadolint at failure threshold `error`: it passes when hadolint reports no errors (warnings are shown but do not fail it). The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
