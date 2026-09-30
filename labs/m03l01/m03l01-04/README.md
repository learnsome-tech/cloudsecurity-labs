# m03l01-04 · A gate that blocks new errors and tolerates old debt

**Lesson:** [Shift-Left Security Principles & Automated Pipeline Gates](https://learnsome.tech/learn/cloudsecurity-course/m03l01) (lesson 3.1, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Graded

## Goal

You can design pull request gates that block new security errors and map each pipeline control to a change management process.

In the lesson: The gate reads a SARIF file and yields the rule, file, line and level of each result. A missing level means warning, which is what the SARIF specification says. Then it counts what main already has, keyed by rule and file. Notice the line number is not in the key. Add one line near the top of a file and every finding below it moves, so a key with line numbers would call old debt new. A finding is new only when this branch has more of that rule in that file than main does, and only new errors block. When anything blocks, the script exits with one, and that non zero exit is what fails the job. In the output, the shell injection in the export tool was already on main, so it is reported but not blocking. The debug warning is new but only a warning. The SQL string built by formatting is new and an error, so the merge stops.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/gate.py`](starter/gate.py): the listing from the lesson
- [`starter/main.sarif`](starter/main.sarif)
- [`starter/pr.sarif`](starter/pr.sarif)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-04/starter`
2. Read `gate.py` the way the lesson builds it:
   - Lines 1–9: reads a SARIF file
   - Lines 10–12: counts what main already has
   - Lines 13–19: A finding is new only
   - Lines 20–21: exits with one
3. Notes from the lesson:
   - Line 12: Key is rule and file; line numbers move on every edit
4. Run it: `python3 gate.py main.sarif pr.sarif`.
5. Check it from the repository root: `./check m03l01-04`.

## Expected output

```text
existing error   subprocess-shell-true   tools/export.py:88
new      warning debug-enabled           app/main.py:12
new      error   formatted-sql-query     app/db.py:47
gate: 1 new error(s), merge blocked
```

## How to check

`./check m03l01-04` copies `starter/` into a scratch directory and runs `python3 gate.py main.sarif pr.sarif` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
