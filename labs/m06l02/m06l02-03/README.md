# m06l02-03 · The evidence behind credential exfiltration

**Lesson:** [Threat Detection with GuardDuty & Anomaly Analytics](https://learnsome.tech/learn/cloudsecurity-course/m06l02) (lesson 6.2, module 6: Cloud Detection, Encryption & Compliance) · Pro  
**Check:** Graded

## Goal

You can read a GuardDuty finding, reproduce the evidence behind it from CloudTrail, explain what an anomaly baseline flags and misses, and route findings with an EventBridge pattern that does not drop the quiet ones.

In the lesson: You should be able to check a finding like that yourself, in CloudTrail, before you wake anyone. When a role reaches an instance through its instance profile, the session name is the instance I D. So every record from that session should come from the instance's own addresses. These few lines apply that rule. It is not GuardDuty's code, it is the same idea. First, map every instance to its private and public address, from a describe instances response. Then walk the CloudTrail records and keep only instance profile sessions. Skip records whose source is a service name, such as S three calling K M S on the role's behalf. Anything else from a foreign address means the keys have left the machine. The first two lines are normal, one of them through a V P C endpoint. The last three lines are someone at another address checking who they are, then looking around.

## Files

- [`starter/cloudtrail.json`](starter/cloudtrail.json)
- [`starter/exfil.py`](starter/exfil.py): the listing from the lesson
- [`starter/instances.json`](starter/instances.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l02/m06l02-03/starter`
2. Read `exfil.py` the way the lesson builds it:
   - Lines 1–7: first, map every instance
   - Lines 8–13: then walk the CloudTrail records
   - Lines 14–18: skip records whose source
   - Lines 19–21: anything else
3. Notes from the lesson:
   - Line 18: Calls AWS makes for the role show a service name, not an IP
4. Run it: `python3 exfil.py`.
5. Check it from the repository root: `./check m06l02-03`.

## Expected output

```text
08:59:12 198.51.100.20 GetParameters            own address
09:02:40 10.0.1.15     GetSecretValue           own address
09:13:58 203.0.113.99  GetCallerIdentity        off the instance
09:14:02 203.0.113.99  ListBuckets              off the instance
09:14:30 203.0.113.99  ListAttachedRolePolicies off the instance
```

## How to check

`./check m06l02-03` copies `starter/` into a scratch directory and runs `python3 exfil.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
