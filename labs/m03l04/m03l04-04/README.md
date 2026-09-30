# m03l04-04 · Matching pinned versions against advisory ranges

**Lesson:** [Software Composition Analysis with Trivy](https://learnsome.tech/learn/cloudsecurity-course/m03l04) (lesson 3.4, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Graded

## Goal

You can match pinned dependencies against OSV advisory ranges, gate a Trivy report with severity thresholds and expiring waivers, and place composition analysis within the four Cs of cloud native security.

In the lesson: Trivy is not installed here, so these are a few lines of Python applying the same matching to that lockfile and two real advisories. The function v turns a version into a tuple of numbers. That only works for plain releases; real tools implement the full Python versioning rules, with pre releases and epochs. Fix for walks the events in introduced and fixed pairs, and returns the fix when the pinned version sits inside a pair. The main loop reads the pins with a regular expression, then checks each advisory in the folder against them. Two findings. Requests two point twenty eight point two is inside the proxy header leak range, moderate, fixed in two point thirty one. U R L lib three is inside the first range of the cookie leak, high. A real database holds more advisories for these old versions than the two in this folder, so a real scan of these pins would report more.

## Files

- [`starter/advisories/GHSA-j8r2-6x86-q33q.json`](starter/advisories/GHSA-j8r2-6x86-q33q.json)
- [`starter/advisories/GHSA-v845-jxx5-vc9f.json`](starter/advisories/GHSA-v845-jxx5-vc9f.json)
- [`starter/requirements.txt`](starter/requirements.txt)
- [`starter/sca_match.py`](starter/sca_match.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-04/starter`
2. Read `sca_match.py` the way the lesson builds it:
   - Lines 1–4: The function v turns
   - Lines 5–9: Fix for walks the events
   - Lines 10–20: The main loop reads the pins
3. Run it: `python3 sca_match.py`.
4. Check it from the repository root: `./check m03l04-04`.

## Expected output

```text
requests 2.28.2  CVE-2023-32681  MODERATE  fixed in 2.31.0
urllib3 1.26.15  CVE-2023-43804  HIGH  fixed in 1.26.17
```

## How to check

`./check m03l04-04` copies `starter/` into a scratch directory and runs `python3 sca_match.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
