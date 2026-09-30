# m04l03-02 · Default deny, then give back DNS

**Lesson:** [Kubernetes NetworkPolicies & Microsegmentation](https://learnsome.tech/learn/cloudsecurity-course/m04l03) (lesson 4.3, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Checker

## Goal

You can write default-deny NetworkPolicies with the egress a namespace really needs, and predict from the YAML alone which pod-to-pod connections they allow.

In the lesson: Start every namespace with a default deny. An empty pod selector matches every pod in shop, both policy types are listed, and there are no rules, so everything in and out is refused. The second policy gives egress back, carefully. Pods may talk to any pod in shop, and they may reach kube DNS in kube system on port fifty three, over U D P and T C P. Forget that DNS rule and every pod fails name resolution, which usually shows up as timeouts rather than an obvious network error. Notice how the namespace is chosen: by the kubernetes dot io slash metadata dot name label. The A P I server sets it on every namespace to the namespace's own name, so a user cannot create another namespace that matches it.

## Files

- [`starter/default-deny.yaml`](starter/default-deny.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-02/starter`
2. Read `default-deny.yaml` the way the lesson builds it:
   - Lines 1–6: default deny
   - Lines 7–15: any pod in shop
   - Lines 16–21: kube DNS
3. Notes from the lesson:
   - Line 5: Empty selector: selects every pod in shop
   - Line 18: Set by the API server on every namespace, cannot be spoofed
4. Edit `default-deny.yaml` and check it: `kubeconform -strict -summary default-deny.yaml`.
5. Check it from the repository root: `./check m04l03-02`.

## How to check

`./check m04l03-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary default-deny.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
