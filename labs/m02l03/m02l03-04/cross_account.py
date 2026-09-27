# Cloud Security & DevSecOps Engineering — lesson m02l03 — Cross-Account AssumeRole Chains & Temporary STS
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l03
# © LearnSome.tech
from sts_sim import assume_role

ci = "arn:aws:sts::111122223333:assumed-role/ci-deployer/run-4812"
sandbox = "arn:aws:sts::111122223333:assumed-role/dev-sandbox/run-4812"
may_assume = {"Statement": [{"Effect": "Allow", "Action": "sts:AssumeRole",
              "Resource": "arn:aws:iam::444455556666:role/prod-*"}]}
prod = "arn:aws:iam::444455556666:role/prod-deploy"
audit = "arn:aws:iam::444455556666:role/vendor-audit"

for label, who, arn, secs in [
        ("ci-deployer to prod-deploy", ci, prod, 3600),
        ("same, for two hours", ci, prod, 7200),
        ("ci-deployer to vendor-audit", ci, audit, 3600),
        ("dev-sandbox to prod-deploy", sandbox, prod, 3600)]:
    print(f"{label:28} {assume_role(who, may_assume, arn, 'run-4812', secs)}")
