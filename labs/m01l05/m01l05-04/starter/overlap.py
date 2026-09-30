import json
from ipaddress import ip_network
from itertools import combinations

def name(vpc):
    return next(t["Value"] for t in vpc["Tags"] if t["Key"] == "Name")

vpcs = {name(v): [ip_network(a["CidrBlock"])      # primary and secondary
                  for a in v["CidrBlockAssociationSet"]]
        for v in json.load(open("vpcs.json"))["Vpcs"]}

for (a, nets_a), (b, nets_b) in combinations(vpcs.items(), 2):
    clash = [f"{x} and {y}" for x in nets_a for y in nets_b if x.overlaps(y)]
    if clash:
        print(f"cannot peer {a} with {b}: {', '.join(clash)}")
