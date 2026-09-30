# m05l02-05 · The caller's side: querying the decision API

**Lesson:** [Policy-as-Code Architecture: OPA & Rego Syntax](https://learnsome.tech/learn/cloudsecurity-course/m05l02) (lesson 5.2, module 5: Infrastructure as Code & Policy-as-Code) · Pro  
**Check:** Graded

## Goal

You can read a Rego policy, predict its decision for a given input including undefined results, and query a decision service so that the caller fails closed.

In the lesson: Now the enforcement side. This client starts a small stand in server, from a sibling file, that answers with the same request and response shape as OPA's data A P I. You post a JSON body with an input key to slash v one slash data, followed by the rule's path. The query function does exactly that with the standard library. It then asks about Ben reading the H R records bucket twice: once at the right path, and once with buckets missing its final s. The right path returns result false, from the default. The typo returns an empty object, because an undefined document comes back with no result key at all, and OPA does not treat that as an error. Now compare the verdicts. The naive check, anything not false is allowed, lets Ben in. Only a check that demands result true fails closed.

## Files

- [`starter/opa_standin.py`](starter/opa_standin.py)
- [`starter/pep.py`](starter/pep.py): the listing from the lesson
- [`starter/rules.py`](starter/rules.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-05/starter`
2. Read `pep.py` the way the lesson builds it:
   - Lines 1–7: starts a small stand in server
   - Lines 8–13: the query function does exactly that
   - Lines 14–22: asks about Ben reading
3. Notes from the lesson:
   - Line 19: anything not false: an empty answer lets Ben in
   - Line 20: fail closed: only an explicit true allows
4. Run it: `python3 pep.py`.
5. Check it from the repository root: `./check m05l02-05`.

## Expected output

```text
platform/buckets/allow: {"result": false} naive=False closed=False
platform/bucket/allow: {} naive=True closed=False
```

## How to check

`./check m05l02-05` copies `starter/` into a scratch directory and runs `python3 pep.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
