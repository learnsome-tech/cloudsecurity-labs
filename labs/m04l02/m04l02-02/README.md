# m04l02-02 · Labelling a namespace for a staged rollout

**Lesson:** [Kubernetes Pod Security Standards: Baseline & Restricted](https://learnsome.tech/learn/cloudsecurity-course/m04l02) (lesson 4.2, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Checker

## Goal

You can label a namespace for Pod Security Admission, predict which pods Baseline and Restricted will reject, and roll enforcement out without breaking workloads.

In the lesson: The shop namespace carries six labels, all under the pod security dot kubernetes dot io prefix. Enforce is set to baseline, so any pod that breaks Baseline is rejected today. Its rules are pinned to a version, v one point three four, which means upgrading the cluster will not quietly change what gets blocked. Then warn and audit are both set to restricted at latest. Nothing is blocked by those two. Warn sends a warning back to whoever ran kubectl apply, and audit adds an annotation to the matching event in the A P I server audit log. This is the normal way to move a namespace up a level: enforce what you already meet, and watch what the next level would say.

## Files

- [`starter/namespace.yaml`](starter/namespace.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-02/starter`
2. Read `namespace.yaml` the way the lesson builds it:
   - Lines 1–5: The shop namespace
   - Lines 6–8: Enforce is set to baseline
   - Lines 9–13: warn and audit
3. Notes from the lesson:
   - Line 8: Pinned: a cluster upgrade cannot tighten the rules by surprise
   - Line 10: Warnings come back to kubectl at apply time
4. Edit `namespace.yaml` and check it: `kubeconform -strict -summary namespace.yaml`.
5. Check it from the repository root: `./check m04l02-02`.

## How to check

`./check m04l02-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary namespace.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
