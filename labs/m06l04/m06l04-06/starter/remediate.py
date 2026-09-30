import datetime
from controls import CONTROLS, ITEMS

TODAY = datetime.date(2026, 9, 27)      # fixed, so the run is repeatable
MAX_CHANGES = 3                         # a bigger plan waits for a person
ACTIONS = {"AWS::EC2::SecurityGroup": "revoke world-open admin rules on",
           "AWS::S3::Bucket": "turn on all four public access blocks for"}

plan = []
for ci in ITEMS:
    if not list(CONTROLS[ci["resourceType"]](ci)):
        continue
    until = ci["tags"].get("cspm-exception")
    if until and datetime.date.fromisoformat(until) >= TODAY:
        print(f"skip   {ci['resourceName']}: exception until {until}")
    elif ci["tags"].get("managed-by") == "terraform":
        print(f"ticket {ci['resourceName']}: Terraform owns it, fix the code")
    else:
        plan.append(f"{ACTIONS[ci['resourceType']]} {ci['resourceId']}")
if len(plan) > MAX_CHANGES:
    raise SystemExit(f"{len(plan)} changes, limit {MAX_CHANGES}: page someone")
print("dry run, would:", *plan, sep="\n  ")
