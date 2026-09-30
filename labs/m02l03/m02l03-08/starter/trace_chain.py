import json

records = json.load(open("trail.json"))["Records"]
issued = {r["responseElements"]["assumedRoleUser"]["arn"]: r
          for r in records if r["eventName"].startswith("AssumeRole")}

event = next(r for r in records if r["eventName"] == "PutBucketPolicy")
who = event["userIdentity"]
print(event["eventTime"], event["eventName"], "by", who["arn"])
while who.get("arn") in issued:
    hop = issued[who["arn"]]
    who = hop["userIdentity"]
    caller = who.get("arn") or f"{who['type']} {who['userName']}"
    print(hop["eventTime"], hop["eventName"], "from", caller)
