# m04l04 · Runtime Anomaly Detection with Falco & eBPF

Module 4: Container & Kubernetes Runtime Defense · lesson 4.4 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m04l04)

**Goal:** You can write and tune Falco rules that turn container syscalls into alerts, and explain how a behavioural baseline and drift detection catch what signature rules miss.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l04-03](m04l04-03/) | Two custom Falco rules | Checker |
| [m04l04-04](m04l04-04/) | Applying the rules to a captured event stream | Graded |
| [m04l04-05](m04l04-05/) | Behavioural baseline and drift | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: write a rule and break the baseline

1. Add an event where python3 spawns sh; predict the alert, then add python3 to WEB and rerun.
2. Write a third rule for connect to port 4444 outside 192.0.2.0/24 and feed it an event.
3. Move the Redis connection into learn.jsonl and confirm the false positive disappears.
4. Add a rule output field user.uid and show the <NA> problem, then add the field to events.

> **Hint:** Use the ipaddress module for the network test. A missing field raises KeyError in this script, where Falco itself would print <NA>.

## Check yourself

- Cat reading the service account token raised an alert, but gunicorn opening the same file did not. Which part of the condition made the difference, and what risk does that exception carry?
- The application wrote no log line when sh -c id ran. Why could Falco still see it, and which fields told you it came from the web server?
- The baseline flagged a connection to 192.0.2.30 port 6379 twenty minutes after the attack. How would you decide whether it is malicious?
- What does proc.is_exe_upper_layer being true tell you, and why is it a strong signal in a container built from an immutable image?
- You need a default Falco rule to include user.uid in its output. Where do you make that change, and why not in falco_rules.yaml?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
