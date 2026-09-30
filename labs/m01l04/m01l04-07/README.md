# m01l04-07 · Reading the server name from a real Client Hello

**Lesson:** [Security Landing Zones & Centralized Egress Inspection](https://learnsome.tech/learn/cloudsecurity-course/m01l04) (lesson 1.4, module 1: Multi-Account Cloud Architecture & Isolation) · Free  
**Check:** Graded

## Goal

You can describe the baseline a security landing zone gives every new account, review Kubernetes control plane and kubelet flags against CIS benchmark expectations, and explain what a centralised domain allow list really inspects and how it can be bypassed.

In the lesson: What does the firewall actually see? The client hello function makes Python's own T L S library start a real handshake in memory and returns the first bytes it would send, the Client Hello. No server exists, so the handshake stops there. The sni function walks that message the way a firewall does: skip the record and handshake headers, the version, the random value and the session I D, then the cipher suites and compression methods, then step through extensions until type zero, the server name. The allowed function applies the two matching rules from the rule group. We run five hostnames through it. The subdomain and the bare domain pass, and so does pypi. Look at evilexample dot com. It ends in example dot com, yet it is dropped, because a leading dot target only matches at a dot boundary.

## Files

- [`starter/egress-domain-allowlist.json`](starter/egress-domain-allowlist.json)
- [`starter/sni.py`](starter/sni.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-07/starter`
2. Read `sni.py` the way the lesson builds it:
   - Lines 1–7: client hello function
   - Lines 8–14: the sni function
   - Lines 15–17: the allowed function
   - Lines 18–22: five hostnames
3. Run it: `python3 sni.py`.
4. Check it from the repository root: `./check m01l04-07`.

## Expected output

```text
sni updates.example.com  pass
sni example.com          pass
sni evilexample.com      drop
sni pypi.org             pass
sni paste.example.net    drop
```

## How to check

`./check m01l04-07` copies `starter/` into a scratch directory and runs `python3 sni.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
