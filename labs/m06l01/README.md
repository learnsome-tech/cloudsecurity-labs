# m06l01 · CloudTrail Logging, Integrity Validation & Athena

Module 6: Cloud Detection, Encryption & Compliance · lesson 6.1 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m06l01)

**Goal:** You can design a CloudTrail trail whose logs survive an intruder, prove with signed digests whether a log file was altered, query the archive with Athena, and write and read a Kubernetes API server audit policy.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l01-02](m06l01-02/) | One record: somebody switches the trail off | Read along |
| [m06l01-03](m06l01-03/) | Signing an hour of log files, the way CloudTrail does | Graded |
| [m06l01-04](m06l01-04/) | Deleting one record, then forging the digest | Graded |
| [m06l01-05](m06l01-05/) | Asking the archive a question with Athena | Read along |
| [m06l01-07](m06l01-07/) | An audit policy: the first matching rule wins | Checker |
| [m06l01-08](m06l01-08/) | Reading the audit log with jq | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Extend the validator and the audit queries

1. In validate.py, delete a whole log file and make validate() report it as missing
2. Predict first: what should validation say if the intruder deletes digest.sig?
3. Add a jq query listing every forbidden request with its verb, resource and namespace
4. Add a RequestResponse rule for pods/exec to the policy; decide where in the order it goes

> **Hint:** sha256() raises FileNotFoundError for a deleted file: test Path.exists() before hashing.

## Check yourself

- An intruder deletes one record from a delivered CloudTrail log file. Which check catches it, and why does rewriting the digest not help them?
- Why should the trail's bucket live in a separate log archive account rather than in the workload account?
- An Athena query over a year of CloudTrail logs is slow and expensive. What change to the table and the query fixes that?
- Your audit policy logs secrets at RequestResponse. What is the risk, and which level should that rule use?
- A request to create a ClusterRoleBinding matches no rule in the audit policy. What is recorded, and how do you prevent that?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
