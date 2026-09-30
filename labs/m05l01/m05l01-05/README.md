# m05l01-05 · A custom check in Checkov's YAML policy format

**Lesson:** [Static IaC Scanning: Linting Terraform with Checkov](https://learnsome.tech/learn/cloudsecurity-course/m05l01) (lesson 5.1, module 5: Infrastructure as Code & Policy-as-Code) · Pro  
**Check:** Checker

## Goal

You can read Checkov findings on a Terraform file, explain the logic behind a check such as CKV_AWS_24, wire the scan's exit code into a pipeline gate, and add a custom YAML check.

In the lesson: Built in checks cover what everyone agrees on. Your own rules, such as every storage resource must say how sensitive its data is, belong in custom checks. This one uses Checkov's YAML policy format. The metadata gives it an I D and a name, and both appear in the report next to the built in findings. The definition joins two attribute conditions with and: the data classification tag must exist, and its value must be one of four agreed labels. A bucket tagged secret, or not tagged at all, fails. You point Checkov at the folder with the external checks dir flag, as the comment on the first line shows. The next two lessons enforce the same tag against a Terraform plan, where it decides which encryption and region rules apply.

## Files

- [`starter/data_classification.yaml`](starter/data_classification.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-05/starter`
2. Read `data_classification.yaml` the way the lesson builds it:
   - Lines 1–5: the metadata gives it an I D
   - Lines 6–16: the definition joins two attribute conditions
3. Edit `data_classification.yaml` and check it: `yamllint data_classification.yaml`.
4. Check it from the repository root: `./check m05l01-05`.

## How to check

`./check m05l01-05` copies `starter/` into a scratch directory and runs `yamllint data_classification.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it lints the YAML with yamllint's `relaxed` rules: it passes when there are no errors. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
