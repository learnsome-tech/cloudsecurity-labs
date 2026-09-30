# m04l04-04 · Applying the rules to a captured event stream

**Lesson:** [Runtime Anomaly Detection with Falco & eBPF](https://learnsome.tech/learn/cloudsecurity-course/m04l04) (lesson 4.4, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Graded

## Goal

You can write and tune Falco rules that turn container syscalls into alerts, and explain how a behavioural baseline and drift detection catch what signature rules miss.

In the lesson: Falco is not installed here, so these are a few lines of Python that apply the same two rules to a captured stream of seven events, written with Falco's own field names. Same lists, then the two conditions translated by hand, and the output templates copied from the YAML. Each match is printed in Falco's text output format: time, priority, then the filled in output. We get two alerts. Gunicorn starting sh dash c id, which is the injection. Then cat reading the token. Look at what stayed quiet. Gunicorn reading its own token is excluded by design. The bash started by runc is an engineer using kubectl exec; our rule ignores it, but Falco's default rule for a terminal shell in a container would catch it. And the host S S H login is not in a container at all.

## Files

- [`starter/events.jsonl`](starter/events.jsonl)
- [`starter/falco_match.py`](starter/falco_match.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-04/starter`
2. Read `falco_match.py` the way the lesson builds it:
   - Lines 1–5: same lists
   - Lines 6–17: two conditions
   - Lines 18–22: text output format
3. Run it: `python3 falco_match.py`.
4. Check it from the repository root: `./check m04l04-04`.

## Expected output

```text
10:02:14.118320951: Warning Shell under web server (parent=gunicorn cmdline=sh -c id pod=web-7d9c)
10:02:15.402117730: Error Token read (proc=cat file=/var/run/secrets/kubernetes.io/serviceaccount/token pod=web-7d9c)
```

## How to check

`./check m04l04-04` copies `starter/` into a scratch directory and runs `python3 falco_match.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
