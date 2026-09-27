# Cloud Security & DevSecOps Engineering — lesson m06l02 — Threat Detection with GuardDuty & Anomaly Analytics
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m06l02
# © LearnSome.tech
import ipaddress, json

own = {}
for reservation in json.load(open("instances.json"))["Reservations"]:
    for inst in reservation["Instances"]:
        own[inst["InstanceId"]] = {inst["PrivateIpAddress"],
                                   inst.get("PublicIpAddress")}

for rec in json.load(open("cloudtrail.json"))["Records"]:
    who = rec["userIdentity"]
    session = who["arn"].rsplit("/", 1)[-1]
    if who["type"] != "AssumedRole" or session not in own:
        continue                     # not an instance profile session
    source = rec["sourceIPAddress"]
    try:
        ipaddress.ip_address(source)
    except ValueError:
        continue                     # an AWS service acting for the role
    where = "own address" if source in own[session] else "off the instance"
    print(rec["eventTime"][11:19], source.ljust(13), rec["eventName"].ljust(24),
          where)
