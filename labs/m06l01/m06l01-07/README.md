# m06l01-07 · An audit policy: the first matching rule wins

**Lesson:** [CloudTrail Logging, Integrity Validation & Athena](https://learnsome.tech/learn/cloudsecurity-course/m06l01) (lesson 6.1, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Checker

## Goal

You can design a CloudTrail trail whose logs survive an intruder, prove with signed digests whether a log file was altered, query the archive with Athena, and write and read a Kubernetes API server audit policy.

In the lesson: The policy is an ordered list of rules, and the first rule that matches a request decides its level. So the order is the design. Omit stages drops the request received stage, which cuts volume without losing anything you would search for. The first rule silences watch requests from kube proxy, which tell you nothing. The second rule matters most, in real clusters and in the exam. Secrets and config maps are logged at metadata only. Put them at request or request response and the log file ends up holding every secret value, so anyone who can read the logs can read the secrets. The third rule records full bodies for changes to R B A C, because when someone grants themselves cluster admin you want the exact binding. The last rule is the catch all at metadata. Without it, a request that no rule matches is not logged at all.

## Files

- [`starter/audit-policy.yaml`](starter/audit-policy.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-07/starter`
2. Read `audit-policy.yaml` the way the lesson builds it:
   - Lines 1–4: omit stages
   - Lines 5–8: the first rule silences
   - Lines 9–13: the second rule matters most
   - Lines 14–18: the third rule records
   - Lines 19–20: the last rule is the catch all
3. Edit `audit-policy.yaml` and check it: `kubeconform -strict -summary audit-policy.yaml`.
4. Check it from the repository root: `./check m06l01-07`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m06l01-07 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary audit-policy.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary audit-policy.yaml`

## How to check

`./check m06l01-07` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary audit-policy.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
