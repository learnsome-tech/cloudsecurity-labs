# m03l02-05 · A pre-commit hook that refuses the commit

**Lesson:** [Pre-Commit Secret Scanning with Gitleaks & Entropy](https://learnsome.tech/learn/cloudsecurity-course/m03l02) (lesson 3.2, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Graded

## Goal

You can write a gitleaks rule that combines a token pattern with an entropy floor, enforce it in a pre-commit hook, and respond correctly when a secret reaches git history.

In the lesson: Now wire it into git. The script creates a repository and ignores your global git config, so nothing on this machine changes the result. Then comes the hook itself: an executable file called pre commit in the hooks folder. Git runs it before recording a commit, and aborts if it exits non zero. The hook pipes the staged diff, with no context lines, into the scanner. Next, the script generates a fake token, stages a client file containing it, and tries to commit. The hook reports the token, the commit is refused with exit status one, and git log confirms there are no commits. The last two lines use the no verify flag, which skips the hook entirely, and the commit goes through. That is the limit of any client side hook: it protects people who want protecting. The same scan has to run in the pipeline, and ideally as push protection on the server.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/fake_token.py`](starter/fake_token.py)
- [`starter/hook.sh`](starter/hook.sh): the listing from the lesson
- [`starter/scan_staged.py`](starter/scan_staged.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-05/starter`
2. Read `hook.sh` the way the lesson builds it:
   - Lines 1–3: The script creates a repository
   - Lines 4–8: Then comes the hook itself
   - Lines 9–14: the script generates a fake token
   - Lines 15–17: use the no verify flag
3. Notes from the lesson:
   - Line 6: -U0: only the changed lines, no context
4. Run it: `bash hook.sh`.
5. Check it from the repository root: `./check m03l02-05`.

## Expected output

```text
client.py:1 exampleorg-api-token exmp_WKbs...REDACTED
commit refused, exit 1
no commits yet
committed anyway
Add API client
```

## How to check

`./check m03l02-05` copies `starter/` into a scratch directory and runs `bash hook.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
