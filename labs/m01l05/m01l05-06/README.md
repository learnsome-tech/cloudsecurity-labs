# m01l05-06 · A data perimeter from both sides of an endpoint

**Lesson:** [Cloud Network Isolation: VPC Peering & PrivateLink](https://learnsome.tech/learn/cloudsecurity-course/m01l05) (lesson 1.5, module 1: Multi-Account Cloud Architecture & Isolation) · Free  
**Check:** Checker

## Goal

You can trace a packet through peered VPC route tables, spot CIDR overlaps that block peering, and choose between peering and PrivateLink by what each one exposes.

In the lesson: Endpoints also carry policies, and together with a bucket policy they form a data perimeter. This CloudFormation template creates a gateway endpoint for S three in the data V P C. First, the endpoint policy. It only allows requests to buckets owned by our own organisation, so a compromised host cannot copy data into an attacker's bucket through this endpoint. Second, the bucket policy on the exports bucket. It denies every object request that did not arrive through this endpoint, whoever is asking, so a stolen access key used from a laptop is refused. Test a deny like this carefully before you apply it, because it also blocks console access and any A W S service reading the bucket on your behalf. That is exactly the point, and exactly how people lock themselves out.

## Files

- [`starter/perimeter.yaml`](starter/perimeter.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-06/starter`
2. Read `perimeter.yaml` the way the lesson builds it:
   - Lines 1–12: the endpoint policy
   - Lines 13–20: the bucket policy
3. Edit `perimeter.yaml` and check it: `yamllint perimeter.yaml`.
4. Check it from the repository root: `./check m01l05-06`.

## How to check

`./check m01l05-06` copies `starter/` into a scratch directory and runs `yamllint perimeter.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it lints the YAML with yamllint's `relaxed` rules: it passes when there are no errors. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
