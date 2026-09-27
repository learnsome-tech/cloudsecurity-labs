# Cloud Security & DevSecOps Engineering — lesson m01l03 — Service Control Policies & Guardrail Architecture
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m01l03
# © LearnSome.tech
from decide import decide, load

PATH = {"Root": load("FullAWSAccess", "DenyLeaveOrg"),
        "Workloads": load("FullAWSAccess", "EuRegionsOnly"),
        "Prod": load("FullAWSAccess", "ProtectCloudTrail"),
        "payments-prod": load("FullAWSAccess")}
CALLS = [("ec2:RunInstances", "eu-west-1", "developer"),
         ("ec2:RunInstances", "us-west-2", "developer"),
         ("iam:CreateRole", "us-east-1", "developer"),
         ("cloudtrail:StopLogging", "eu-west-1", "developer"),
         ("cloudtrail:StopLogging", "eu-west-1", "platform-admin"),
         ("organizations:LeaveOrganization", "us-east-1", "platform-admin")]

for action, region, role in CALLS:
    req = {"action": action, "aws:RequestedRegion": region,
           "aws:PrincipalARN": f"arn:aws:iam::444444444444:role/{role}"}
    verb = action.split(":")[1]
    print(f"{verb:17} {region:9} {role:14} {decide(PATH, req)}")
