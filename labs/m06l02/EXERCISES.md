# Exercises — Threat Detection with GuardDuty & Anomaly Analytics

Lesson `m06l02` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m06l02)

## Exercise 1: Tune the detector and fix the route

1. Add a $or to high-severity.json so the Stealth finding also pages, and teach matches() $or
2. In anomaly.py, predict dev-sam's line if UpdateFunctionConfiguration joins the history
3. Add an app-server record from 10.0.2.31, the other instance, to cloudtrail.json; flagged?
4. Change the /24 network to /16 in anomaly.py; which true positives do you lose?

> **Hint**: EventBridge $or takes a list of sub-patterns; the event matches if any one matches.


---

© LearnSome.tech · support@iwantto.learnsome.tech
