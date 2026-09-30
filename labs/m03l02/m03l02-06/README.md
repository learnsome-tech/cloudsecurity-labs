# m03l02-06 · Deleted from the file, still in the history

**Lesson:** [Pre-Commit Secret Scanning with Gitleaks & Entropy](https://learnsome.tech/learn/cloudsecurity-course/m03l02) (lesson 3.2, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Graded

## Goal

You can write a gitleaks rule that combines a token pattern with an entropy floor, enforce it in a pre-commit hook, and respond correctly when a secret reaches git history.

In the lesson: Here is the mistake everyone makes after a leak. The repository gets fixed dates so the commit ids repeat. The first commit adds the fake token. The second replaces it with a read from an environment variable, which is the right fix for the code. Now look at the evidence. Grep on the working tree finds nothing, so the file looks clean. But git log with the dash G option lists every commit whose diff adds or removes a match for the pattern, and it shows both commits. Then the whole history is fed to the same scanner through git log with patches, which is how gitleaks walks a repository's past. The token is found at line one of the client file, in the first commit. Anyone with a clone can run git show on that commit and read it.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/fake_token.py`](starter/fake_token.py)
- [`starter/history.sh`](starter/history.sh): the listing from the lesson
- [`starter/scan_staged.py`](starter/scan_staged.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-06/starter`
2. Read `history.sh` the way the lesson builds it:
   - Lines 1–4: gets fixed dates
   - Lines 5–9: The first commit adds
   - Lines 10–13: git log with the dash G option
   - Lines 14–15: the whole history is fed
3. Run it: `bash history.sh`.
4. Check it from the repository root: `./check m03l02-06`.

## Expected output

```text
in the working tree: 0 matches
commits that added or removed a token:
  c893501 Read the token from the environment
  dde4c90 Add API client
whole history, as gitleaks reads it:
client.py:1 exampleorg-api-token exmp_WKbs...REDACTED
```

## How to check

`./check m03l02-06` copies `starter/` into a scratch directory and runs `bash history.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
