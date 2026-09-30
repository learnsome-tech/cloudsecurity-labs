# m03l05-03 · Answering a new advisory from stored SBOMs

**Lesson:** [Supply Chain Security: SBOMs & Cosign Signing](https://learnsome.tech/learn/cloudsecurity-course/m03l05) (lesson 3.5, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Graded

## Goal

You can produce and query CycloneDX SBOMs, sign and verify an image digest the way cosign does, and roll out signature enforcement as a controlled change.

In the lesson: Here is where an S B O M pays for itself. A new advisory arrives for U R L lib three: every release before one point twenty six point seventeen, plus two point zero point zero up to two point zero point five. Instead of rescanning every image, query the bills of materials you already keep. This jq program takes the image name from the metadata, selects the U R L lib three component, splits its version into numbers so that arrays compare numerically, then tests both ranges. It runs across all four stored files in one go. The A P I image and the web image are affected. The worker is on a fixed release. The reports image does not appear at all, because it does not ship that library. That answer matters as much as the others: without an S B O M, proving you are not affected means scanning every image again.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/query.sh`](starter/query.sh): the listing from the lesson
- [`starter/sboms/api.cdx.json`](starter/sboms/api.cdx.json)
- [`starter/sboms/reports.cdx.json`](starter/sboms/reports.cdx.json)
- [`starter/sboms/web.cdx.json`](starter/sboms/web.cdx.json)
- [`starter/sboms/worker.cdx.json`](starter/sboms/worker.cdx.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-03/starter`
2. Read `query.sh` the way the lesson builds it:
   - Lines 1–2: A new advisory arrives
   - Lines 3–10: This jq program takes
3. Run it: `bash query.sh`.
4. Check it from the repository root: `./check m03l05-03`.

## Expected output

```text
registry.example.com/shop/api  urllib3 1.26.15  affected
registry.example.com/shop/web  urllib3 2.0.4  affected
registry.example.com/shop/worker  urllib3 1.26.18  not affected
```

## How to check

`./check m03l05-03` copies `starter/` into a scratch directory and runs `bash query.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
