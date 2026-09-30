# m04l02 · Kubernetes Pod Security Standards: Baseline & Restricted

Module 4: Container & Kubernetes Runtime Defense · lesson 4.2 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m04l02)

**Goal:** You can label a namespace for Pod Security Admission, predict which pods Baseline and Restricted will reject, and roll enforcement out without breaking workloads.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l02-02](m04l02-02/) | Labelling a namespace for a staged rollout | Checker |
| [m04l02-03](m04l02-03/) | The checks, written out in Python | Read along |
| [m04l02-04](m04l02-04/) | An ordinary pod against both levels | Graded |
| [m04l02-05](m04l02-05/) | What a Restricted-compliant pod spec looks like | Read along |
| [m04l02-06](m04l02-06/) | Pre-flight: what breaks if we enforce Restricted? | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: extend the checker and predict

1. Add a Baseline hostPorts check to pss.py, give log-agent a hostPort, and rerun admit.py.
2. Move seccompProfile from pod level to the container in hardened-pod.json; predict the result.
3. Add the Restricted rule that capabilities.add may contain only NET_BIND_SERVICE.
4. Set hostNetwork to false for node-exporter in pods.json and predict the new tally first.

> **Hint:** Host ports sit in each container's ports list as hostPort. The merged security context means container-level settings count just as pod-level ones do.

## Check yourself

- A Deployment applied cleanly to a namespace enforcing restricted, yet it has zero ready pods. Why did the apply succeed, and where is the evidence?
- The web pod passed Baseline but failed Restricted four times. What does that tell you about what each level is designed to catch?
- Why does the namespace enforce baseline while setting warn and audit to restricted, instead of enforcing restricted straight away?
- The node exporter needs hostPID, hostNetwork and a hostPath mount. Why is moving it to its own namespace better than lowering shop to privileged?
- hardened-pod.json sets runAsNonRoot and seccompProfile only at pod level. Why does the container still pass those checks, and why can't allowPrivilegeEscalation be set the same way?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
