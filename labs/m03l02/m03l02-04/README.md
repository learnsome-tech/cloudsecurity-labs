# m03l02-04 · Applying the same rule to a staged diff

**Lesson:** [Pre-Commit Secret Scanning with Gitleaks & Entropy](https://learnsome.tech/learn/cloudsecurity-course/m03l02) (lesson 3.2, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Graded

## Goal

You can write a gitleaks rule that combines a token pattern with an entropy floor, enforce it in a pre-commit hook, and respond correctly when a secret reaches git history.

In the lesson: Gitleaks is not installed here, so this is a few lines of Python that apply the rule from that TOML file to a staged diff. At the top sit the same regular expression and the same fixtures allowlist. The entropy function is the one you just saw. The loop reads a unified diff, the format git diff produces. A line starting with three plus signs names the file, a hunk header gives the starting line number, and every added line is checked: keyword, then pattern, then entropy of the token, then the allowlist. A hit prints the file, line and rule, with the token cut short so the scanner's own output does not leak it. It exits with one on any hit. The diff holds three candidates. The fake key in the client file is reported. The row of x characters in the docs matches the pattern but scores zero. The fixture token is random, but allowlisted.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/scan_staged.py`](starter/scan_staged.py): the listing from the lesson
- [`starter/staged.diff`](starter/staged.diff)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-04/starter`
2. Read `scan_staged.py` the way the lesson builds it:
   - Lines 1–5: the same regular expression
   - Lines 6–8: The entropy function
   - Lines 9–21: The loop reads a unified diff
   - Lines 22: It exits with one
3. Run it: `python3 scan_staged.py staged.diff`.
4. Check it from the repository root: `./check m03l02-04`.

## Expected output

```text
app/client.py:6 exampleorg-api-token exmp_HWii...REDACTED
```

## How to check

`./check m03l02-04` copies `starter/` into a scratch directory and runs `python3 scan_staged.py staged.diff` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
