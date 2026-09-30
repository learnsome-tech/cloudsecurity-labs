# m03l03-03 · The grep approach, and why developers stop reading it

**Lesson:** [Static Application Security Testing with Semgrep](https://learnsome.tech/learn/cloudsecurity-course/m03l03) (lesson 3.3, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Graded

## Goal

You can explain why syntax-aware SAST beats text matching, read and write a Semgrep rule for SQL built from strings, and route findings through an owned asset inventory.

In the lesson: First, the grep approach, written as a few lines of Python so you can see exactly what it matches. The regular expression looks for execute, followed later on the same line by a percent sign, a plus, a format call or an f string. The loop tests every line and prints the ones that match. Read the four results against what you now know. Line four is a real finding. Line eight is the safe parameterised query, flagged because its placeholder contains a percent sign. Line seventeen is a comment. Line eighteen is real. So two of the four are false positives, and the injectable search function on line thirteen is missing entirely, because the dangerous string and the execute call sit on different lines. A developer who sees output like this twice stops reading it.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/db.py`](starter/db.py)
- [`starter/grep_scan.py`](starter/grep_scan.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-03/starter`
2. Read `grep_scan.py` the way the lesson builds it:
   - Lines 1–4: The regular expression looks for
   - Lines 5–8: The loop tests every line
3. Run it: `python3 grep_scan.py db.py`.
4. Check it from the repository root: `./check m03l03-03`.

## Expected output

```text
db.py:4  cur.execute("SELECT name FROM users WHERE id = %s" % user_id)
db.py:8  cur.execute("SELECT id FROM users WHERE email = %s", (email,))
db.py:17  # was: cur.execute("SELECT count(*) FROM %s" % table)
db.py:18  cur.execute(f"SELECT count(*) FROM {table}")
```

## How to check

`./check m03l03-03` copies `starter/` into a scratch directory and runs `python3 grep_scan.py db.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
