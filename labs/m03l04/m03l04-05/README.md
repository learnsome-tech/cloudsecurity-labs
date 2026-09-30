# m03l04-05 · A gate with severity and expiring waivers

**Lesson:** [Software Composition Analysis with Trivy](https://learnsome.tech/learn/cloudsecurity-course/m03l04) (lesson 3.4, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Graded

## Goal

You can match pinned dependencies against OSV advisory ranges, gate a Trivy report with severity thresholds and expiring waivers, and place composition analysis within the four Cs of cloud native security.

In the lesson: A list of findings is not a decision, so here is a gate over a Trivy JSON report holding the same two findings. Trivy writes this format when you pass format json. Today is fixed so the output does not drift. Block holds high and critical, the same effect as passing those two severities with an exit code of one. Next, the ignore file: each line holds a vulnerability id and an optional expiry, written exp, a colon and a date, which is Trivy's own dot trivyignore syntax. Our file waives the U R L lib three finding until the end of June, with an owner and a reason in the comments. Then each finding is waived, blocking, or reported. Look at the result. Requests is medium, so it is reported but does not block. The U R L lib three waiver expired in June, so the high finding is back and the build fails. Accepted risk comes back for review instead of living forever.

## Files

- [`starter/.trivyignore`](starter/.trivyignore)
- [`starter/command.txt`](starter/command.txt)
- [`starter/report.json`](starter/report.json)
- [`starter/sca_gate.py`](starter/sca_gate.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-05/starter`
2. Read `sca_gate.py` the way the lesson builds it:
   - Lines 1–5: Today is fixed
   - Lines 6–8: Next, the ignore file
   - Lines 9–22: Then each finding is
3. Notes from the lesson:
   - Line 8: No exp: date means the waiver never expires
4. Run it: `python3 sca_gate.py report.json`.
5. Check it from the repository root: `./check m03l04-05`.

## Expected output

```text
requests 2.28.2 CVE-2023-32681 MEDIUM: reported
urllib3 1.26.15 CVE-2023-43804 HIGH: blocking (waiver expired 2026-06-30)
1 blocking finding(s)
```

## How to check

`./check m03l04-05` copies `starter/` into a scratch directory and runs `python3 sca_gate.py report.json` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
