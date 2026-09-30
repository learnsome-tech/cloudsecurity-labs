# m04l04-03 · Two custom Falco rules

**Lesson:** [Runtime Anomaly Detection with Falco & eBPF](https://learnsome.tech/learn/cloudsecurity-course/m04l04) (lesson 4.4, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Checker

## Goal

You can write and tune Falco rules that turn container syscalls into alerts, and explain how a behavioural baseline and drift detection catch what signature rules miss.

In the lesson: Custom rules belong in falco rules dot local dot yaml, which loads after the default file and survives upgrades. We start with a list of web server process names. The first rule uses three default macros: spawned process, meaning an execve that returned, container, meaning not the host, and shell procs, meaning the name is a known shell. Then our own check that the parent is a web server. Output is the alert text; each word after a percent sign is a field filled in from the event. The priority is warning, one of eight levels from emergency down to debug. The second rule fires when any process other than the web server opens a file in the service account directory, which is what an attacker does before calling the Kubernetes A P I with the pod's identity.

## Files

- [`starter/falco_rules.local.yaml`](starter/falco_rules.local.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-03/starter`
2. Read `falco_rules.local.yaml` the way the lesson builds it:
   - Lines 1–3: a list
   - Lines 4–13: first rule
   - Lines 14–22: second rule
3. Notes from the lesson:
   - Line 8: Macros from the default falco_rules.yaml
   - Line 10: %fields are filled in from the event
   - Line 12: One of eight syslog-style priorities
4. Edit `falco_rules.local.yaml` and check it: `yamllint falco_rules.local.yaml`.
5. Check it from the repository root: `./check m04l04-03`.
6. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m04l04-03 --command=<id>`:
   - `lint` (Lint): `yamllint -d relaxed falco_rules.local.yaml`
   - `strict` (Lint strictly): `yamllint falco_rules.local.yaml`

## How to check

`./check m04l04-03` copies `starter/` into a scratch directory and runs `yamllint falco_rules.local.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it lints the YAML with yamllint's `relaxed` rules: it passes when there are no errors. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
