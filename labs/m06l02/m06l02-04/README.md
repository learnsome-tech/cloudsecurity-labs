# m06l02-04 · Anomaly analytics: a baseline per identity

**Lesson:** [Threat Detection with GuardDuty & Anomaly Analytics](https://learnsome.tech/learn/cloudsecurity-course/m06l02) (lesson 6.2, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Graded

## Goal

You can read a GuardDuty finding, reproduce the evidence behind it from CloudTrail, explain what an anomaly baseline flags and misses, and route findings with an EventBridge pattern that does not drop the quiet ones.

In the lesson: Rules like that catch a known pattern. Anomaly detection asks a different question: is this normal for this identity? GuardDuty builds that baseline with its own models over more signals than we use here, so treat this as the idea in miniature. Two small helpers load records and turn an address into its network. From two weeks of history, record which calls each identity makes and from which networks. Then score today. The build bot updating its service from the usual runner network is baseline. The same build bot listing buckets, reading a bucket policy and listing users, all within a minute from a network it has never used, is stolen keys doing discovery. The last line is dev sam calling a Lambda A P I for the first time, from the usual office network. That is a developer shipping a feature. New is not the same as malicious, and every anomaly system pays for that in false positives.

## Files

- [`starter/anomaly.py`](starter/anomaly.py): the listing from the lesson
- [`starter/history.json`](starter/history.json)
- [`starter/today.json`](starter/today.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l02/m06l02-04/starter`
2. Read `anomaly.py` the way the lesson builds it:
   - Lines 1–8: two small helpers
   - Lines 9–14: from two weeks of history
   - Lines 15–21: then score today
3. Run it: `python3 anomaly.py`.
4. Check it from the repository root: `./check m06l02-04`.

## Expected output

```text
09:00 build-bot UpdateService               baseline
09:31 dev-sam   GetLogEvents                baseline
09:41 build-bot ListBuckets                 new call, new network 192.0.2.0/24
09:41 build-bot GetBucketPolicy             new call, new network 192.0.2.0/24
09:41 build-bot ListUsers                   new call, new network 192.0.2.0/24
10:02 dev-sam   UpdateFunctionConfiguration new call
```

## How to check

`./check m06l02-04` copies `starter/` into a scratch directory and runs `python3 anomaly.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
