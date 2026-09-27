# Cloud Security & DevSecOps Engineering — lesson m02l04 — Least Privilege Enforcement & CIEM Architecture
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l04
# © LearnSome.tech
import json
from fnmatch import fnmatchcase
from iam_eval import many

PATHS = {
    "new version of a policy": ["iam:CreatePolicyVersion"],
    "attach a policy to a role": ["iam:AttachRolePolicy"],
    "Lambda runs as a passed role": ["iam:PassRole", "lambda:CreateFunction",
                                     "lambda:InvokeFunction"],
    "EC2 runs as a passed role": ["iam:PassRole", "ec2:RunInstances"],
}

def allows(policy, action):  # ignores resources and conditions: over-reports
    return any(st["Effect"] == "Allow" and any(
        fnmatchcase(action.lower(), p.lower()) for p in many(st["Action"]))
        for st in policy["Statement"])

for role, policy in json.load(open("role-policies.json")).items():
    found = [path for path, needs in PATHS.items()
             if all(allows(policy, action) for action in needs)]
    print(f"{role:14} {'; '.join(found) or 'no known path'}")
