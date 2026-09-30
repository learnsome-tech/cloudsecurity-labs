# m04l01-05 · Rootless: what container root is on the host

**Lesson:** [Container Hardening: Distroless & Rootless](https://learnsome.tech/learn/cloudsecurity-course/m04l01) (lesson 4.1, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Graded

## Goal

You can build a distroless, non-root image and prove from process status and ID maps what an attacker inside it can and cannot do.

In the lesson: Rootless means two different things, and people mix them up. One is what we just did: the process inside runs as a non root user. The other is a user namespace, where even root inside the container is an unprivileged user outside it. The kernel publishes the mapping in proc self uid map as three numbers per line: first id inside, first id outside, and how many. This helper translates a container U I D to the host U I D. We compare two maps. With no user namespace the map is identity, so container root is host root, and a breakout lands as root on the node. With a user namespace, container root is host U I D one hundred thousand, and anything outside the range is not mapped at all. Kubernetes exposes this per pod with host users set to false, where the node supports it.

## Files

- [`starter/no-userns.uid_map`](starter/no-userns.uid_map)
- [`starter/uidmap.py`](starter/uidmap.py): the listing from the lesson
- [`starter/userns.uid_map`](starter/userns.uid_map)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-05/starter`
2. Read `uidmap.py` the way the lesson builds it:
   - Lines 1–3: three numbers
   - Lines 4–9: translates a container
   - Lines 10–16: two maps
3. Notes from the lesson:
   - Line 2: Same format as /proc/self/uid_map inside the container
4. Run it: `python3 uidmap.py`.
5. Check it from the repository root: `./check m04l01-05`.

## Expected output

```text
no-userns.uid_map: container uid     0 is host uid 0
no-userns.uid_map: container uid 65532 is host uid 65532
no-userns.uid_map: container uid 70000 is host uid 70000
userns.uid_map: container uid     0 is host uid 100000
userns.uid_map: container uid 65532 is host uid 165532
userns.uid_map: container uid 70000 is not mapped
```

## How to check

`./check m04l01-05` copies `starter/` into a scratch directory and runs `python3 uidmap.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
