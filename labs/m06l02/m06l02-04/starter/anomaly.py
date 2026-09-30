import ipaddress, json
from collections import defaultdict

def records(name):
    return json.load(open(name))["Records"]

def network(rec):
    return ipaddress.ip_network(rec["sourceIPAddress"] + "/24", strict=False)

apis, nets = defaultdict(set), defaultdict(set)
for rec in records("history.json"):          # fourteen days of normal
    who = rec["userIdentity"]["arn"]
    apis[who].add(rec["eventName"])
    nets[who].add(network(rec))

for rec in records("today.json"):
    who = rec["userIdentity"]["arn"]
    new = [] if rec["eventName"] in apis[who] else ["new call"]
    new += [] if network(rec) in nets[who] else [f"new network {network(rec)}"]
    print(rec["eventTime"][11:16], who.rsplit("/", 1)[-1].ljust(9),
          rec["eventName"].ljust(27), ", ".join(new) or "baseline")
