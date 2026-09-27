# Cloud Security & DevSecOps Engineering — lesson m02l04 — Least Privilege Enforcement & CIEM Architecture
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l04
# © LearnSome.tech
from collections import defaultdict
from iam_eval import decide
from trail import calls

by_scope = defaultdict(set)
for action, scope in calls("trail-90d.json", "reporting-app"):
    by_scope[scope].add(action)
policy = {"Version": "2012-10-17", "Statement": [
    {"Effect": "Allow", "Action": sorted(actions), "Resource": scope}
    for scope, actions in sorted(by_scope.items())]}
for st in policy["Statement"]:
    print(", ".join(st["Action"]), "on", st["Resource"].split(":")[-1])

for action, resource in [
        ("s3:GetObject", "arn:aws:s3:::example-reports/monthly/2026-10.csv"),
        ("s3:GetObject", "arn:aws:s3:::example-payroll/2026-09.csv"),
        ("s3:DeleteBucket", "arn:aws:s3:::example-reports")]:
    verdict = decide(policy, action, resource, {})
    print(f"{action:16} {resource.split(':')[-1]:36} {verdict}")
