# m04l03 · Kubernetes NetworkPolicies & Microsegmentation

Module 4: Container & Kubernetes Runtime Defense · lesson 4.3 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m04l03)

**Goal:** You can write default-deny NetworkPolicies with the egress a namespace really needs, and predict from the YAML alone which pod-to-pod connections they allow.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l03-02](m04l03-02/) | Default deny, then give back DNS | Checker |
| [m04l03-03](m04l03-03/) | How the plugin decides, in twenty lines | Read along |
| [m04l03-04](m04l03-04/) | Walking six connections through the policies | Graded |
| [m04l03-05](m04l03-05/) | The one-dash difference: AND versus OR | Checker |
| [m04l03-06](m04l03-06/) | Proving what the extra dash opened up | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: open, close and break a flow

1. Predict, then run: add connect('web', 'kube-dns', 53) to flows.py.
2. Delete the DNS rule from shop-policies.json and predict which lines of output change.
3. Add an ingress policy so Prometheus can scrape db on 8081; check debug-shell stays blocked.
4. Label the shop namespace team: monitoring in pods.json and rerun and_or.py; explain the result.

> **Hint:** Namespace labels live in each pod's ns_labels entry. A pod in shop that also matches the namespace selector satisfies version A without being Prometheus.

## Check yourself

- Web to db was blocked even though web's egress allowed it. Which half failed, and which policy would you change to allow it?
- After applying default-deny with no DNS rule, pods report timeouts talking to other services by name. Why?
- In the scrape policy, what exactly does version B allow that version A does not?
- Why is the kubernetes.io/metadata.name label a safer namespace selector than a label like team: monitoring?
- You apply a default-deny policy and a connection that should fail still succeeds. What is the first thing to check?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
