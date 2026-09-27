# Cloud Security & DevSecOps Engineering — lesson m01l03 — Service Control Policies & Guardrail Architecture
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m01l03
# © LearnSome.tech
from decide import decide, load

# Someone swapped FullAWSAccess on Workloads for a short allow list
PATH = {"Root": load("FullAWSAccess"),
        "Workloads": load("AllowComputeAndStorage"),
        "Prod": load("FullAWSAccess"),
        "payments-prod": load("FullAWSAccess")}

for action in ["ec2:RunInstances", "s3:GetObject", "kms:Decrypt",
               "logs:PutLogEvents", "sts:AssumeRole"]:
    req = {"action": action, "aws:RequestedRegion": "eu-west-1",
           "aws:PrincipalARN": "arn:aws:iam::444444444444:role/orders-app"}
    print(f"{action:18} {decide(PATH, req)}")
