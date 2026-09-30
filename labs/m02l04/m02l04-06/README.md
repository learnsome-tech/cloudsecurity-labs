# m02l04-06 · Looking for privilege escalation paths

**Lesson:** [Least Privilege Enforcement & CIEM Architecture](https://learnsome.tech/learn/cloudsecurity-course/m02l04) (lesson 2.4, module 2: Cloud Identity & Zero-Trust Governance) · Pro  
**Check:** Graded

## Goal

You can measure the gap between granted and used permissions, generate a right-sized policy from CloudTrail, and flag privilege escalation paths.

In the lesson: Unused access is one risk. Escalation paths are another: sets of permissions that together let an identity grant itself more. Public research has catalogued many of them, and here are four well known paths. Creating a new version of a policy lets you rewrite a policy you are attached to. Attaching a policy to a role hands out administrator access. Passing a role to a Lambda function or an instance lets your code run as that role. Next, the allows function asks whether any allow statement matches an action. It ignores resources and conditions, so it reports too much rather than too little. Then each role is checked against every path. The C I deployer shows the Lambda path. Platform ops, holding all of I A M and E C two, shows three. The reporting app and the analyst show none.

## Files

- [`starter/escalate.py`](starter/escalate.py): the listing from the lesson
- [`starter/iam_eval.py`](starter/iam_eval.py)
- [`starter/role-policies.json`](starter/role-policies.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-06/starter`
2. Read `escalate.py` the way the lesson builds it:
   - Lines 1–11: four well known paths
   - Lines 12–16: the allows function
   - Lines 17–21: then each role is checked
3. Notes from the lesson:
   - Line 13: Resource scope and conditions are ignored, so results over-report
4. Run it: `python3 escalate.py`.
5. Check it from the repository root: `./check m02l04-06`.

## Expected output

```text
reporting-app  no known path
ci-deployer    Lambda runs as a passed role
platform-ops   new version of a policy; attach a policy to a role; EC2 runs as a passed role
data-analyst   no known path
```

## How to check

`./check m02l04-06` copies `starter/` into a scratch directory and runs `python3 escalate.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
