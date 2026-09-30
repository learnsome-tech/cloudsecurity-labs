# m04l04-05 · Behavioural baseline and drift

**Lesson:** [Runtime Anomaly Detection with Falco & eBPF](https://learnsome.tech/learn/cloudsecurity-course/m04l04) (lesson 4.4, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Graded

## Goal

You can write and tune Falco rules that turn container syscalls into alerts, and explain how a behavioural baseline and drift detection catch what signature rules miss.

In the lesson: Signature rules only catch what someone predicted. Behavioural analytics asks a different question: is this workload doing something it has never done before? Each event becomes one short string, either the program executed or the address and port it connected to. During a learning window we record everything the web image did: run gunicorn, call DNS, call Postgres. Three behaviours. In the watch window, anything else is reported. The shell is new. The next exec is worse: Falco's is exe upper layer field says the binary lives in the container's writable layer, so it was dropped at runtime and was never in the image. That is drift, and in an immutable container it is almost always hostile. Then a connection to port four four four four outside. The last line, six three seven nine, is a Redis cache added by a deploy, which shows the cost.

## Files

- [`starter/baseline.py`](starter/baseline.py): the listing from the lesson
- [`starter/learn.jsonl`](starter/learn.jsonl)
- [`starter/watch.jsonl`](starter/watch.jsonl)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-05/starter`
2. Read `baseline.py` the way the lesson builds it:
   - Lines 1–7: one short string
   - Lines 8–13: learning window
   - Lines 14–20: watch window
3. Notes from the lesson:
   - Line 17: Executable came from the container's writable layer
4. Run it: `python3 baseline.py`.
5. Check it from the repository root: `./check m04l04-05`.

## Expected output

```text
learned 3 behaviours for registry.example.com/shop/web
10:02:14.118320951 new: exec /bin/sh
10:02:31.840227613 drift: binary not in the image: exec /tmp/.x/kworker
10:02:32.001958340 new: connect 203.0.113.50:4444
10:20:44.395148200 new: connect 192.0.2.30:6379
```

## How to check

`./check m04l04-05` copies `starter/` into a scratch directory and runs `python3 baseline.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
