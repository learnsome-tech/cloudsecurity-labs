# m04l03-05 · The one-dash difference: AND versus OR

**Lesson:** [Kubernetes NetworkPolicies & Microsegmentation](https://learnsome.tech/learn/cloudsecurity-course/m04l03) (lesson 4.3, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Checker

## Goal

You can write default-deny NetworkPolicies with the egress a namespace really needs, and predict from the YAML alone which pod-to-pod connections they allow.

In the lesson: Prometheus in the monitoring namespace needs to scrape the A P I's metrics port, eighty eighty one. Version A has one entry in the from list, carrying a namespace selector and a pod selector on the same list item. That means both must match: a pod labelled prometheus, in a namespace labelled team monitoring. Version B looks almost identical. The only change is a dash in front of pod selector, which turns it into a second peer. Now the list says: any pod in a monitoring namespace, or any pod labelled prometheus in the policy's own namespace. Code review rarely catches this, because the diff is a single character and both versions apply without complaint.

## Files

- [`starter/scrape.yaml`](starter/scrape.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-05/starter`
2. Read `scrape.yaml` the way the lesson builds it:
   - Lines 1–9: Version A
   - Lines 10–19: Version B
3. Notes from the lesson:
   - Line 9: No dash: same list item, both must match
   - Line 19: Dash: a second peer, either one is enough
4. Edit `scrape.yaml` and check it: `yamllint scrape.yaml`.
5. Check it from the repository root: `./check m04l03-05`.

## How to check

`./check m04l03-05` copies `starter/` into a scratch directory and runs `yamllint scrape.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it lints the YAML with yamllint's `relaxed` rules: it passes when there are no errors. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
