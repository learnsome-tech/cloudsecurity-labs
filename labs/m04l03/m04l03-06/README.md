# m04l03-06 · Proving what the extra dash opened up

**Lesson:** [Kubernetes NetworkPolicies & Microsegmentation](https://learnsome.tech/learn/cloudsecurity-course/m04l03) (lesson 4.3, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Graded

## Goal

You can write default-deny NetworkPolicies with the egress a namespace really needs, and predict from the YAML alone which pod-to-pod connections they allow.

In the lesson: We evaluate both versions on top of the default deny, with three callers aiming at the A P I on port eighty eighty one. The real Prometheus gets in under both, so any smoke test you run after deploying passes either way. Under version A, Grafana is blocked, and so is a pod called debug shell that somebody started in shop and labelled app prometheus. Under version B, both get in. Anyone who can create a pod in shop can now reach the metrics port just by choosing a label. The lesson is to test the flows that should fail, not only the one you meant to open.

## Files

- [`starter/and_or.py`](starter/and_or.py): the listing from the lesson
- [`starter/default-deny.json`](starter/default-deny.json)
- [`starter/netpol.py`](starter/netpol.py)
- [`starter/pods.json`](starter/pods.json)
- [`starter/scrape-and.json`](starter/scrape-and.json)
- [`starter/scrape-or.json`](starter/scrape-or.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-06/starter`
2. Read `and_or.py` the way the lesson builds it:
   - Lines 1–5: default deny
   - Lines 6–12: three callers
3. Run it: `python3 and_or.py`.
4. Check it from the repository root: `./check m04l03-06`.

## Expected output

```text
scrape-and.json: prometheus in monitoring -> api:8081 allowed
scrape-and.json: grafana in monitoring -> api:8081 blocked
scrape-and.json: debug-shell in shop -> api:8081 blocked
scrape-or.json: prometheus in monitoring -> api:8081 allowed
scrape-or.json: grafana in monitoring -> api:8081 allowed
scrape-or.json: debug-shell in shop -> api:8081 allowed
```

## How to check

`./check m04l03-06` copies `starter/` into a scratch directory and runs `python3 and_or.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
