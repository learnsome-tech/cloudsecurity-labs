# m03l01-05 · Version control as the change record and the backout

**Lesson:** [Shift-Left Security Principles & Automated Pipeline Gates](https://learnsome.tech/learn/cloudsecurity-course/m03l01) (lesson 3.1, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Runs, not graded

## Goal

You can design pull request gates that block new security errors and map each pipeline control to a change management process.

In the lesson: Version control is the audit trail for a change, and it also holds the backout plan. This script builds a fresh repository with fixed dates, so the hashes come out the same every run. The first commit is the approved state: egress to one payments range on port four hundred and forty three. The second is the risky change, which opens that port to any address. Its message carries two trailers, Approved by and Backout, so the approval and the undo plan travel with the change instead of living in a ticket nobody links. Then the on call engineer reverts it. Revert does not erase anything. It adds a new commit that applies the opposite change, so the log shows who opened the rule, who approved it and who backed it out. The file ends up where it started. Rewrite history instead, and that evidence is gone.

## Files

- [`starter/backout.sh`](starter/backout.sh): the listing from the lesson
- [`starter/command.txt`](starter/command.txt)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-05/starter`
2. Read `backout.sh` the way the lesson builds it:
   - Lines 1–4: builds a fresh repository
   - Lines 5–7: is the approved state
   - Lines 8–12: The second is the risky change
   - Lines 13–16: the on call engineer reverts
3. Notes from the lesson:
   - Line 11: Trailers: approval and backout plan stored in the commit
4. Run it: `bash backout.sh`.
5. Check it from the repository root: `./check m03l01-05`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
3d84f91 On-call: Revert "CHG-1042: open egress for vendor webhooks"
86076dd Priya Shah: CHG-1042: open egress for vendor webhooks
Approved-by: Sam Okafor
Backout: git revert, no restart needed
df7d329 Priya Shah: Egress: payments API only
allow 198.51.100.0/24 tcp/443
```

## How to check

`./check m03l01-05` copies `starter/` into a scratch directory and runs `bash backout.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
