# m04l01-04 · Reading capabilities out of proc status

**Lesson:** [Container Hardening: Distroless & Rootless](https://learnsome.tech/learn/cloudsecurity-course/m04l01) (lesson 4.1, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Graded

## Goal

You can build a distroless, non-root image and prove from process status and ID maps what an attacker inside it can and cannot do.

In the lesson: Inside a running container you can read proc self status. The Cap lines are what the kernel will actually allow. The list at the top is the kernel's own numbering, so CHOWN is bit zero and SETFCAP is bit thirty one. Each Cap line is a hex bitmask, and decode turns set bits into names, the same job capsh dash dash decode does. We read three processes captured from the same image. Run as root with Docker's defaults, it holds fourteen capabilities, including NET RAW for crafting packets and SETUID for switching users. Run as U I D sixty five thousand five hundred and thirty two, the effective set is empty, but the bounding set still allows fourteen, so a setuid root binary could lift it back. The hardened pod drops all capabilities and sets no new privs, and both sets are empty.

## Files

- [`starter/capdecode.py`](starter/capdecode.py): the listing from the lesson
- [`starter/hardened.status`](starter/hardened.status)
- [`starter/nonroot.status`](starter/nonroot.status)
- [`starter/root.status`](starter/root.status)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-04/starter`
2. Read `capdecode.py` the way the lesson builds it:
   - Lines 1–8: kernel's own numbering
   - Lines 9–12: a hex bitmask
   - Lines 13–22: three processes
3. Notes from the lesson:
   - Line 2: List index is the capability number: CHOWN is bit zero
   - Line 16: Bounding set: the ceiling a process can ever reach
4. Run it: `python3 capdecode.py`.
5. Check it from the repository root: `./check m04l01-04`.

## Expected output

```text
root.status: uid 0, NoNewPrivs 0, bounding 14, effective 14
  CHOWN DAC_OVERRIDE FOWNER FSETID KILL SETGID SETUID SETPCAP
  NET_BIND_SERVICE NET_RAW SYS_CHROOT MKNOD AUDIT_WRITE SETFCAP
nonroot.status: uid 65532, NoNewPrivs 0, bounding 14, effective 0
hardened.status: uid 65532, NoNewPrivs 1, bounding 0, effective 0
```

## How to check

`./check m04l01-04` copies `starter/` into a scratch directory and runs `python3 capdecode.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
