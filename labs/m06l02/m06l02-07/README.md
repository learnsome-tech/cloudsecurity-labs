# m06l02-07 · Routing four findings, and the one that gets lost

**Lesson:** [Threat Detection with GuardDuty & Anomaly Analytics](https://learnsome.tech/learn/cloudsecurity-course/m06l02) (lesson 6.2, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Graded

## Goal

You can read a GuardDuty finding, reproduce the evidence behind it from CloudTrail, explain what an anomaly baseline flags and misses, and route findings with an EventBridge pattern that does not drop the quiet ones.

In the lesson: EventBridge only runs in A W S, so here is a small Python version of its matching rules, just the exact value and numeric comparison this pattern uses. Test handles one value: a numeric rule compares, anything else must be equal. Matches walks the pattern, recursing into nested blocks, and every field must find at least one acceptable value. Now run it over four findings. Credential exfiltration and the Bitcoin D N S lookup are both eight, so they page. The port probe is two and waits in the queue, which is fine. The last line is the problem. Someone disabled CloudTrail logging, the stop logging call from the last lesson, and GuardDuty rates it low. A pure severity rule files the first move of an intruder under routine.

## Files

- [`starter/events.json`](starter/events.json)
- [`starter/high-severity.json`](starter/high-severity.json)
- [`starter/route.py`](starter/route.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l02/m06l02-07/starter`
2. Read `route.py` the way the lesson builds it:
   - Lines 1–7: test handles one value
   - Lines 8–17: matches walks the pattern
   - Lines 18–22: run it over four findings
3. Run it: `python3 route.py`.
4. Check it from the repository root: `./check m06l02-07`.

## Expected output

```text
page  8 UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration.OutsideAWS
queue 2 Recon:EC2/PortProbeUnprotectedPort
page  8 CryptoCurrency:EC2/BitcoinTool.B!DNS
queue 2 Stealth:IAMUser/CloudTrailLoggingDisabled
```

## How to check

`./check m06l02-07` copies `starter/` into a scratch directory and runs `python3 route.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
