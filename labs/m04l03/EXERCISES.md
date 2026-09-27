# Exercises — Kubernetes NetworkPolicies & Microsegmentation

Lesson `m04l03` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m04l03)

## Exercise 1: Your turn: open, close and break a flow

1. Predict, then run: add connect('web', 'kube-dns', 53) to flows.py.
2. Delete the DNS rule from shop-policies.json and predict which lines of output change.
3. Add an ingress policy so Prometheus can scrape db on 8081; check debug-shell stays blocked.
4. Label the shop namespace team: monitoring in pods.json and rerun and_or.py; explain the result.

> **Hint**: Namespace labels live in each pod's ns_labels entry. A pod in shop that also matches the namespace selector satisfies version A without being Prometheus.


---

© LearnSome.tech · support@iwantto.learnsome.tech
