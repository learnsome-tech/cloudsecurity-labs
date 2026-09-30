# m04l05-06 · What etcd holds with and without encryption

**Lesson:** [Securing the Kubernetes Control Plane & Node Components](https://learnsome.tech/learn/cloudsecurity-course/m04l05) (lesson 4.5, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Graded

## Goal

You can audit API server and kubelet settings against CIS-style checks, and turn on and verify encryption at rest for Secrets in etcd.

In the lesson: Here is the real transformation, using openssl for the A E S. The Secret is shown as J S O N for readability; the A P I server actually stores protobuf, but the password bytes are just as visible. The key and I V are fixed so the output repeats; the real provider picks a random I V for every write. Note the storage prefix: k eight s, enc, aescbc, v one, then the key name. We encrypt with openssl enc in C B C mode and store prefix, I V and ciphertext, exactly the layout the aescbc provider uses. Then we print both stored forms. Identity: the password readable, true. Aescbc: the prefix in clear, then noise. The prefix is how you verify the setting worked: read the key with etcdctl on the control plane and check it starts with k eight s enc. Then we decrypt with key one to prove nothing was lost.

## Files

- [`starter/etcd_at_rest.py`](starter/etcd_at_rest.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-06/starter`
2. Read `etcd_at_rest.py` the way the lesson builds it:
   - Lines 1–7: storage prefix
   - Lines 8–12: openssl enc
   - Lines 13–21: both stored forms
3. Run it: `python3 etcd_at_rest.py`.
4. Check it from the repository root: `./check m04l05-06`.

## Expected output

```text
identity: 56 bytes, password readable: True
  {"kind":"Secret","data":{"password":"ZXhhbXBsZS1vbmx5"}}
aescbc: 103 bytes, password readable: False
  k8s:enc:aescbc:v1:key1:...................*.....*(......h..J
decrypted with key1: b'{"kind":"Secret","data":{"password":'
```

## How to check

`./check m04l05-06` copies `starter/` into a scratch directory and runs `python3 etcd_at_rest.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
