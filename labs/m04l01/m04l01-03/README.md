# m04l01-03 · Command injection with and without a shell

**Lesson:** [Container Hardening: Distroless & Rootless](https://learnsome.tech/learn/cloudsecurity-course/m04l01) (lesson 4.1, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Graded

## Goal

You can build a distroless, non-root image and prove from process status and ID maps what an attacker inside it can and cannot do.

In the lesson: Here is the injection itself, for real, on this machine. We make two directories standing in for image filesystems. The slim one has bin sh linked to a real shell; the distroless one has an empty bin. Then the vulnerable helper: it pastes a file name into a shell command. Python's shell equals true runs bin sh by absolute path, which is what os dot system does too, so we point that path into each image. The same payload goes to both: a file name, a semicolon, and the attacker's own command. In slim, both commands ran. In distroless, the exec failed with no such file or directory. The bug is identical. The outcome is not. Notice what distroless does not stop, though: code that runs inside the Python interpreter itself, such as an unsafe pickle load, needs no shell at all.

## Files

- [`starter/thumbnail.py`](starter/thumbnail.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-03/starter`
2. Read `thumbnail.py` the way the lesson builds it:
   - Lines 1–8: two directories
   - Lines 9–15: the vulnerable helper
   - Lines 16–22: same payload
3. Notes from the lesson:
   - Line 8: slim image: bin sh points at a real shell
   - Line 13: shell=True execs /bin/sh by path, as os.system does
4. Run it: `python3 thumbnail.py`.
5. Check it from the repository root: `./check m04l01-03`.

## Expected output

```text
slim ['resizing cat.png', 'attacker command ran']
distroless exec failed: No such file or directory distroless/bin/sh
```

## How to check

`./check m04l01-03` copies `starter/` into a scratch directory and runs `python3 thumbnail.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
