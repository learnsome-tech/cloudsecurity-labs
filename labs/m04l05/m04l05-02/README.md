# m04l05-02 · The API server's static pod manifest

**Lesson:** [Securing the Kubernetes Control Plane & Node Components](https://learnsome.tech/learn/cloudsecurity-course/m04l05) (lesson 4.5, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Checker

## Goal

You can audit API server and kubelet settings against CIS-style checks, and turn on and verify encryption at rest for Secrets in etcd.

In the lesson: On a kubeadm cluster the A P I server runs as a static pod. The kubelet on the control plane node reads this file from etc kubernetes manifests and restarts the server whenever it changes, so the flags in the command list are the security configuration. Some of it is good. Authorisation mode is Node and R B A C, so the Node authoriser keeps each kubelet to the objects of pods on its own node, and R B A C governs everyone else. The NodeRestriction admission plugin stops a kubelet from modifying other nodes or setting protected labels on its own node object. Now notice what is missing. There is no anonymous auth flag, no profiling flag, no audit log, no encryption configuration and no certificate authority for checking kubelets. An absent flag is not neutral: it means the default.

## Files

- [`starter/kube-apiserver.yaml`](starter/kube-apiserver.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-02/starter`
2. Read `kube-apiserver.yaml` the way the lesson builds it:
   - Lines 1–10: static pod
   - Lines 11–15: Node and R B A C
   - Lines 16–21: what is missing
3. Notes from the lesson:
   - Line 13: Node authorizer limits kubelets to their own node's objects
   - Line 15: Stops a kubelet editing other nodes or labelling itself
4. Edit `kube-apiserver.yaml` and check it: `kubeconform -strict -summary kube-apiserver.yaml`.
5. Check it from the repository root: `./check m04l05-02`.
6. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m04l05-02 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary kube-apiserver.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary kube-apiserver.yaml`

## How to check

`./check m04l05-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary kube-apiserver.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
