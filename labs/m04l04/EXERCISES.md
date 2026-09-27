# Exercises — Runtime Anomaly Detection with Falco & eBPF

Lesson `m04l04` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m04l04)

## Exercise 1: Your turn: write a rule and break the baseline

1. Add an event where python3 spawns sh; predict the alert, then add python3 to WEB and rerun.
2. Write a third rule for connect to port 4444 outside 192.0.2.0/24 and feed it an event.
3. Move the Redis connection into learn.jsonl and confirm the false positive disappears.
4. Add a rule output field user.uid and show the <NA> problem, then add the field to events.

> **Hint**: Use the ipaddress module for the network test. A missing field raises KeyError in this script, where Falco itself would print <NA>.


---

© LearnSome.tech · support@iwantto.learnsome.tech
