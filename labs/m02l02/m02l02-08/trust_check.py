# Cloud Security & DevSecOps Engineering — lesson m02l02 — Workload Identity Federation: Eliminating Static Keys
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l02
# © LearnSome.tech
import json
from iam_eval import holds  # the condition check from lesson one

HOST = "token.actions.githubusercontent.com"
def trusts(policy, claims):
    ctx = {f"{HOST}:{k}": v for k, v in claims.items()}
    conds = policy["Statement"][0]["Condition"].items()
    return all(holds(op, k, v, ctx) for op, kv in conds for k, v in kv.items())

aud = {f"{HOST}:aud": "sts.amazonaws.com"}
exact = json.load(open("trust-policy.json"))
org = {"Statement": [{"Condition": {"StringEquals": aud,
       "StringLike": {f"{HOST}:sub": "repo:example-org/*"}}}]}
aud_only = {"Statement": [{"Condition": {"StringEquals": aud}}]}
print(f"{'subject':52} exact org   aud-only")
for sub in ["repo:example-org/payments-api:environment:production",
            "repo:example-org/payments-api:pull_request",
            "repo:example-org/sandbox:ref:refs/heads/main",
            "repo:someone-else/tools:ref:refs/heads/main"]:
    claims = {"aud": "sts.amazonaws.com", "sub": sub}
    row = [f"{trusts(p, claims)!s:5}" for p in (exact, org, aud_only)]
    print(f"{sub:52}", *row)
