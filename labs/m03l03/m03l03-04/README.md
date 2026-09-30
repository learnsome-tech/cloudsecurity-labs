# m03l03-04 · Asking the syntax tree instead

**Lesson:** [Static Application Security Testing with Semgrep](https://learnsome.tech/learn/cloudsecurity-course/m03l03) (lesson 3.3, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Graded

## Goal

You can explain why syntax-aware SAST beats text matching, read and write a Semgrep rule for SQL built from strings, and route findings through an owned asset inventory.

In the lesson: Now the same question, asked of the syntax tree. Python's own ast module parses the file into nodes, so a comment never appears at all, and a string literal is one node however many percent signs it contains. The function how built receives the first argument of an execute call. If that argument is a variable, it looks up what was assigned to it. Then it asks: is this an f string, a percent or plus operation, or a format call? A plain literal returns nothing. For each function, the scanner records every assignment in that function, then walks it looking for calls whose method is execute, and asks how the SQL was built. Three results: lines four, thirteen and eighteen, which are exactly the injectable ones. The placeholder and the comment are not reported. That idea, matching code structure rather than text, is what Semgrep is built on.

## Files

- [`starter/ast_scan.py`](starter/ast_scan.py): the listing from the lesson
- [`starter/command.txt`](starter/command.txt)
- [`starter/db.py`](starter/db.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-04/starter`
2. Read `ast_scan.py` the way the lesson builds it:
   - Lines 1–10: The function how built
   - Lines 11–16: records every assignment
   - Lines 17–21: then walks it looking for calls
3. Notes from the lesson:
   - Line 4: A variable is replaced by the value assigned to it
4. Run it: `python3 ast_scan.py db.py`.
5. Check it from the repository root: `./check m03l03-04`.

## Expected output

```text
db.py:4  SQL built by % formatting
db.py:13  SQL built by % formatting
db.py:18  SQL built by an f-string
```

## How to check

`./check m03l03-04` copies `starter/` into a scratch directory and runs `python3 ast_scan.py db.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
