# m06l02 · Threat Detection with GuardDuty & Anomaly Analytics

Module 6: Cloud Detection, Encryption & Compliance · lesson 6.2 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m06l02)

**Goal:** You can read a GuardDuty finding, reproduce the evidence behind it from CloudTrail, explain what an anomaly baseline flags and misses, and route findings with an EventBridge pattern that does not drop the quiet ones.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l02-02](m06l02-02/) | Anatomy of a finding | Read along |
| [m06l02-03](m06l02-03/) | The evidence behind credential exfiltration | Graded |
| [m06l02-04](m06l02-04/) | Anomaly analytics: a baseline per identity | Graded |
| [m06l02-06](m06l02-06/) | An EventBridge rule for high severity findings | Read along |
| [m06l02-07](m06l02-07/) | Routing four findings, and the one that gets lost | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Tune the detector and fix the route

1. Add a $or to high-severity.json so the Stealth finding also pages, and teach matches() $or
2. In anomaly.py, predict dev-sam's line if UpdateFunctionConfiguration joins the history
3. Add an app-server record from 10.0.2.31, the other instance, to cloudtrail.json; flagged?
4. Change the /24 network to /16 in anomaly.py; which true positives do you lose?

> **Hint:** EventBridge $or takes a list of sub-patterns; the event matches if any one matches.

## Check yourself

- An intruder with admin rights stops the trail and deletes the flow logs. Why can GuardDuty still see their next API calls?
- Which CloudTrail fields let you confirm an InstanceCredentialExfiltration finding yourself, and what value proves it?
- Why did the anomaly baseline flag dev-sam's UpdateFunctionConfiguration call, and what does that tell you about anomaly findings?
- A pattern matches severity of seven or more. Which kind of finding does it drop, and how would you change the pattern?
- Why is a suppression rule that archives a whole finding type across every account dangerous?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
