# Cloud Security & DevSecOps Engineering — lesson m02l01 — Cloud IAM Architecture & Permission Boundaries
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l01
# © LearnSome.tech
import json
from iam_eval import decide

policy = json.load(open("app-dev.json"))
data = "arn:aws:s3:::example-app-data"
roles = "arn:aws:iam::111122223333:role"
console = {"aws:MultiFactorAuthPresent": "true"}
access_key = {}  # long-term keys send no MFA key at all

requests = [
    ("s3:GetObject", f"{data}/reports/q3.csv", console),
    ("s3:DeleteBucket", data, console),
    ("s3:DeleteObject", f"{data}/reports/q3.csv", access_key),
    ("iam:CreateRole", f"{roles}/app-reporting", access_key),
]
for action, resource, ctx in requests:
    verdict = decide(policy, action, resource, ctx)
    print(f"{action:16} {resource.split(':')[-1]:32} {verdict}")
