# m04l03-04 · Walking six connections through the policies

**Lesson:** [Kubernetes NetworkPolicies & Microsegmentation](https://learnsome.tech/learn/cloudsecurity-course/m04l03) (lesson 4.3, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Graded

## Goal

You can write default-deny NetworkPolicies with the egress a namespace really needs, and predict from the YAML alone which pod-to-pod connections they allow.

In the lesson: The file holds four policies: the two you just saw, plus api from web, allowing port eighty eighty, and db from api, allowing port five four three two. They are the same objects converted to J S O N, because Python's standard library has no YAML parser. Connect checks both halves and prints each one, which is exactly how you should debug a blocked flow. We try six connections. Web to the A P I is allowed. Web to the database is blocked at ingress: web may send, but the database only accepts the A P I. The A P I reaches the database and DNS. The database calling out to Grafana in another namespace is blocked at egress false, which is what stops a compromised database pod from phoning out. Grafana to web fails at ingress, even though monitoring has no policies of its own.

## Files

- [`starter/flows.py`](starter/flows.py): the listing from the lesson
- [`starter/netpol.py`](starter/netpol.py)
- [`starter/pods.json`](starter/pods.json)
- [`starter/shop-policies.json`](starter/shop-policies.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-04/starter`
2. Read `flows.py` the way the lesson builds it:
   - Lines 1–5: four policies
   - Lines 6–12: both halves
   - Lines 13–19: six connections
3. Run it: `python3 flows.py`.
4. Check it from the repository root: `./check m04l03-04`.

## Expected output

```text
web      -> api:8080         egress True  ingress True  allowed
web      -> db:5432          egress True  ingress False blocked
api      -> db:5432          egress True  ingress True  allowed
api      -> kube-dns:53      egress True  ingress True  allowed
db       -> grafana:3000     egress False ingress True  blocked
grafana  -> web:8080         egress True  ingress False blocked
```

## How to check

`./check m04l03-04` copies `starter/` into a scratch directory and runs `python3 flows.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
