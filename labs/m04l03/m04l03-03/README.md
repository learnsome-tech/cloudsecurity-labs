# m04l03-03 · How the plugin decides, in twenty lines

**Lesson:** [Kubernetes NetworkPolicies & Microsegmentation](https://learnsome.tech/learn/cloudsecurity-course/m04l03) (lesson 4.3, module 4: Container & Kubernetes Runtime Defense) · Pro  
**Check:** Read along

## Goal

You can write default-deny NetworkPolicies with the egress a namespace really needs, and predict from the YAML alone which pod-to-pod connections they allow.

In the lesson: These are a few lines of Python that apply the same decision the C N I plugin makes, limited to match labels and leaving out I P blocks. Selects is plain label matching. A peer matches when its namespace and its pod labels both match. If the peer has no namespace selector, it only covers pods in the policy's own namespace, which surprises people. Allowed first collects the policies in the pod's namespace that select this pod for this direction. None means the pod is not isolated, so the answer is yes. Otherwise we walk every rule in every selecting policy, and any rule whose peers and ports both match lets the traffic in. A missing list of peers or ports means anything. That any at the end is the whole additive model: one matching rule anywhere wins.

## Files

- [`starter/netpol.py`](starter/netpol.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/netpol.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–2: match labels
   - Lines 3–7: A peer matches
   - Lines 8–14: not isolated
   - Lines 15–21: every rule
3. Notes from the lesson:
   - Line 6: No namespaceSelector: only the policy's own namespace
   - Line 17: Missing from, to or ports means anything

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
