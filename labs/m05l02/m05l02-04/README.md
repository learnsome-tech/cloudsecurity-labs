# m05l02-04 · A line-by-line Python mirror of the policy

**Lesson:** [Policy-as-Code Architecture: OPA & Rego Syntax](https://learnsome.tech/learn/cloudsecurity-course/m05l02) (lesson 5.2, module 5: Infrastructure as Code & Policy-as-Code) · Pro  
**Check:** Graded

## Goal

You can read a Rego policy, predict its decision for a given input including undefined results, and query a decision service so that the caller fails closed.

In the lesson: OPA isn't installed here, so this is a line by line Python mirror of the policy. It shows the semantics; it is not the engine. Each allow body becomes one boolean, and the two are combined with or, just as two rules with one name are. Every field lookup uses get, so a missing field gives None and fails the body instead of crashing, which is how Rego treats an undefined path. The deny function builds a set, one message per matching body. Now run it over four requests from the inputs file. Amara from platform is allowed by rule one, yet deny still fires, because she has no M F A. Allow and deny are separate answers, so the caller must read both. The backup service has no team at all, and it gets the default false rather than a crash.

## Files

- [`starter/inputs.json`](starter/inputs.json)
- [`starter/rules.py`](starter/rules.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-04/starter`
2. Read `rules.py` the way the lesson builds it:
   - Lines 1–7: each allow body becomes one boolean
   - Lines 8–13: the deny function builds a set
   - Lines 14–18: over four requests from the inputs file
3. Notes from the lesson:
   - Line 4: get() gives None for a missing field: the body fails
4. Run it: `python3 rules.py`.
5. Check it from the repository root: `./check m05l02-04`.

## Expected output

```text
amara delete logs-archive: allow=True deny=['amara: delete without MFA']
ben read payments-exports: allow=True deny=[]
ben read hr-records: allow=False deny=[]
svc-backup read hr-records: allow=False deny=[]
```

## How to check

`./check m05l02-04` copies `starter/` into a scratch directory and runs `python3 rules.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
