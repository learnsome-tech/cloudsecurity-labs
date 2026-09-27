# Exercises — Kubernetes Pod Security Standards: Baseline & Restricted

Lesson `m04l02` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m04l02)

## Exercise 1: Your turn: extend the checker and predict

1. Add a Baseline hostPorts check to pss.py, give log-agent a hostPort, and rerun admit.py.
2. Move seccompProfile from pod level to the container in hardened-pod.json; predict the result.
3. Add the Restricted rule that capabilities.add may contain only NET_BIND_SERVICE.
4. Set hostNetwork to false for node-exporter in pods.json and predict the new tally first.

> **Hint**: Host ports sit in each container's ports list as hostPort. The merged security context means container-level settings count just as pod-level ones do.


---

© LearnSome.tech · support@iwantto.learnsome.tech
