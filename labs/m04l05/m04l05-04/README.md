# m04l05-04 · Locking down the kubelet

**Lesson:** [Securing the Kubernetes Control Plane & Node Components](https://learnsome.tech/learn/cloudsecurity-course/m04l05) (lesson 4.5, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Checker

## Goal

You can audit API server and kubelet settings against CIS-style checks, and turn on and verify encryption at rest for Secrets in etcd.

In the lesson: The kubelet is the more dangerous one, because it runs on every node and can execute commands in any pod there. Started with no configuration, the kubelet binary accepts anonymous requests and uses AlwaysAllow, so anyone who reaches port ten two five zero can run commands in your containers. kubeadm writes a safer file, but check it. Under authentication, anonymous is disabled, webhook is enabled so bearer tokens are verified with the A P I server, and client certificates must chain to the cluster C A. The authorisation mode is Webhook, which asks the A P I server whether this caller may, for example, create an exec on this node. The read only port is set to zero. Server T L S bootstrap requests a serving certificate signed by the cluster, which is what the kubelet certificate authority flag on the A P I server then verifies.

## Files

- [`starter/config.yaml`](starter/config.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-04/starter`
2. Read `config.yaml` the way the lesson builds it:
   - Lines 1–10: authentication
   - Lines 11–13: authorisation mode
   - Lines 14–16: serving certificate
3. Notes from the lesson:
   - Line 6: Default for a bare kubelet binary is true
   - Line 12: Default for a bare kubelet binary is AlwaysAllow
4. Edit `config.yaml` and check it: `kubeconform -strict -summary config.yaml`.
5. Check it from the repository root: `./check m04l05-04`.
6. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m04l05-04 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary config.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary config.yaml`

## How to check

`./check m04l05-04` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary config.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
