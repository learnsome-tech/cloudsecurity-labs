# m01l04-04 · Checking the flags the way kube-bench does

**Lesson:** [Security Landing Zones & Centralized Egress Inspection](https://learnsome.tech/learn/cloudsecurity-course/m01l04) (lesson 1.4, module 1: Multi-Account Cloud Architecture & Isolation) · Free  
**Check:** Graded

## Goal

You can describe the baseline a security landing zone gives every new account, review Kubernetes control plane and kubelet flags against CIS benchmark expectations, and explain what a centralised domain allow list really inspects and how it can be bypassed.

In the lesson: The real tool for this is kube bench, which runs the benchmark checks on a node. It is not installed here, so this is a few lines of Python applying the same kind of check to the same files. There are seven rules, each naming a component, a flag and the value the benchmark expects, with a dash meaning the flag must be absent. The flags function pulls every double dash name equals value pair out of a file, which works for pod manifests and for the kubelet's systemd line alike. Then, for each rule, it reads the before and after copies and prints the value found and a verdict. Every rule fails before and passes after. Three of them are not on the A P I server: etcd must require client certificates, and the kubelet must refuse anonymous requests and close its unauthenticated read only port.

## Files

- [`starter/after/etcd.yaml`](starter/after/etcd.yaml)
- [`starter/after/kube-apiserver.yaml`](starter/after/kube-apiserver.yaml)
- [`starter/after/kubelet.conf`](starter/after/kubelet.conf)
- [`starter/before/etcd.yaml`](starter/before/etcd.yaml)
- [`starter/before/kube-apiserver.yaml`](starter/before/kube-apiserver.yaml)
- [`starter/before/kubelet.conf`](starter/before/kubelet.conf)
- [`starter/cis.py`](starter/cis.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-04/starter`
2. Read `cis.py` the way the lesson builds it:
   - Lines 1–10: seven rules
   - Lines 11–13: the flags function
   - Lines 14–21: for each rule
3. Run it: `python3 cis.py`.
4. Check it from the repository root: `./check m01l04-04`.

## Expected output

```text
kube-apiserver anonymous-auth     false  true         fail false        ok
kube-apiserver authorization-mode RBAC   AlwaysAllow  fail Node,RBAC    ok
kube-apiserver profiling          false  true         fail false        ok
kube-apiserver token-auth-file    -      /srv/tok.csv fail -            ok
etcd           client-cert-auth   true   false        fail true         ok
kubelet        anonymous-auth     false  true         fail false        ok
kubelet        read-only-port     0      10255        fail 0            ok
```

## How to check

`./check m01l04-04` copies `starter/` into a scratch directory and runs `python3 cis.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
