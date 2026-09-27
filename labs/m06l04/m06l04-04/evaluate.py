# Cloud Security & DevSecOps Engineering — lesson m06l04 — Cloud Security Posture Management & Remediation
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m06l04
# © LearnSome.tech
from controls import CONTROLS, ITEMS

for ci in ITEMS:
    problems = list(CONTROLS[ci["resourceType"]](ci))
    print("NON_COMPLIANT" if problems else "COMPLIANT", ci["resourceName"])
    for problem in problems:
        print("  " + problem)
