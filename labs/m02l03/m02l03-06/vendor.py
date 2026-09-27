# Cloud Security & DevSecOps Engineering — lesson m02l03 — Cross-Account AssumeRole Chains & Temporary STS
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l03
# © LearnSome.tech
from sts_sim import ROLES, assume_role

scanner = "arn:aws:sts::777788889999:assumed-role/vendor-scanner/job-77"
anything = {"Statement": [{"Effect": "Allow", "Action": "sts:AssumeRole",
            "Resource": "*"}]}
victim = "arn:aws:iam::444455556666:role/vendor-audit"
tenants = {"customer-4471, the owner": ("ex-customer-4471", victim),
           "customer-9020, attacker": ("ex-customer-9020", victim)}

def run_jobs():
    for tenant, (external_id, role) in tenants.items():
        result = assume_role(scanner, anything, role, "scan",
                             ctx={"sts:ExternalId": external_id})
        print(f"  {tenant:25} {result}")

print("trust policy requires the ExternalId:")
run_jobs()
del ROLES[victim]["AssumeRolePolicyDocument"]["Statement"][0]["Condition"]
print("trust policy without the condition:")
run_jobs()
