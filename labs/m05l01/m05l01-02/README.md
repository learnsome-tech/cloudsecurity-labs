# m05l01-02 · main.tf: three findings in twenty-two lines

**Lesson:** [Static IaC Scanning: Linting Terraform with Checkov](https://learnsome.tech/learn/cloudsecurity-course/m05l01) (lesson 5.1, module 5: Infrastructure as Code & Policy-as-Code) · Pro  
**Check:** Read along

## Goal

You can read Checkov findings on a Terraform file, explain the logic behind a check such as CKV_AWS_24, wire the scan's exit code into a pipeline gate, and add a custom YAML check.

In the lesson: Here is a file that would pass most human reviews: a bastion security group, and the instance behind it. Checkov flags three things. The ingress block allows port twenty two from anywhere, which is check twenty four. The instance has no metadata options block, so version one of the instance metadata service stays reachable, and a server side request forgery bug in anything on that host could read the instance role's credentials from it. That is check seventy nine. And the root volume is explicitly unencrypted, which is check eight. For each finding, Checkov prints the check I D and its description, the word failed, the resource address such as aws security group dot bastion, and the line range in the file, so the author can jump straight to the block.

## Files

- [`starter/main.tf`](starter/main.tf): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/main.tf` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–12: a bastion security group
   - Lines 13–22: the instance behind it
3. Notes from the lesson:
   - Line 10: CKV_AWS_24: port 22 reachable from 0.0.0.0/0
   - Line 14: CKV_AWS_79: no metadata_options, IMDSv1 stays enabled
   - Line 20: CKV_AWS_8: root EBS volume stored unencrypted

## How to check

**Read along.** Its Terraform configuration uses the `aws` provider, which needs a real cloud account. The lab sandbox has only the local, null and random providers.

There is nothing to check: `./check m05l01-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
