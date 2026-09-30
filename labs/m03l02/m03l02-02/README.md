# m03l02-02 · Measuring randomness with Shannon entropy

**Lesson:** [Pre-Commit Secret Scanning with Gitleaks & Entropy](https://learnsome.tech/learn/cloudsecurity-course/m03l02) (lesson 3.2, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Graded

## Goal

You can write a gitleaks rule that combines a token pattern with an entropy floor, enforce it in a pre-commit hook, and respond correctly when a secret reaches git history.

In the lesson: Scanners find secrets two ways: a pattern for a known token format, and randomness. Randomness is measured with Shannon entropy: how surprising each character is, given how often it appears in the string, averaged and expressed in bits. The function counts characters and sums minus p times log p. Next, a fixed seed builds a fake thirty two character token, so the output is the same every run and nothing real appears on screen. Then there are five strings to compare, and the loop prints each one with its length and score. English words land around three point four. A run of one repeated letter scores zero. Look at the commit id and the UUID, though: both clear three and a half bits, and neither is a secret. Hex can never go above four bits a character. Entropy alone would bury you in false positives; a threshold only makes sense next to a pattern.

## Files

- [`starter/entropy.py`](starter/entropy.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-02/starter`
2. Read `entropy.py` the way the lesson builds it:
   - Lines 1–6: The function counts characters
   - Lines 7–10: a fixed seed builds
   - Lines 11–17: five strings to compare
   - Lines 18–20: the loop prints each one
3. Run it: `python3 entropy.py`.
4. Check it from the repository root: `./check m03l02-02`.

## Expected output

```text
english words  25 chars  3.36 bits per char
placeholder    32 chars  0.00 bits per char
git commit id  40 chars  3.87 bits per char
uuid           36 chars  3.69 bits per char
random base62  32 chars  4.52 bits per char
```

## How to check

`./check m03l02-02` copies `starter/` into a scratch directory and runs `python3 entropy.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
