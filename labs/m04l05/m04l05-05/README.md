# m04l05-05 · Encryption at rest for Secrets

**Lesson:** [Securing the Kubernetes Control Plane & Node Components](https://learnsome.tech/learn/cloudsecurity-course/m04l05) (lesson 4.5, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Checker

## Goal

You can audit API server and kubelet settings against CIS-style checks, and turn on and verify encryption at rest for Secrets in etcd.

In the lesson: Base sixty four is not encryption, and by default a Secret sits in etcd readable by anyone with the database or its backup. This file, passed to the A P I server with the encryption provider config flag, changes that for only Secrets here, though you can list other resources. The first provider encrypts every new write; here that is aescbc with one key named key one. The key is thirty two random bytes, base sixty four encoded, and it lives on the control plane disk, which is the weakness of every local key provider. The identity provider comes last so the server can still read Secrets written before encryption was switched on. The Kubernetes documentation now recommends the K M S version two provider, where the key stays in a cloud key service, and it warns about C B C. We use aescbc here because openssl can show it.

## Files

- [`starter/enc.yaml`](starter/enc.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-05/starter`
2. Read `enc.yaml` the way the lesson builds it:
   - Lines 1–5: only Secrets
   - Lines 6–10: first provider
   - Lines 11: identity provider
3. Notes from the lesson:
   - Line 7: Order matters: the first provider writes, all of them read
4. Edit `enc.yaml` and check it: `kubeconform -strict -summary enc.yaml`.
5. Check it from the repository root: `./check m04l05-05`.

## How to check

`./check m04l05-05` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary enc.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
