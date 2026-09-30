import json, sys

state = json.load(open("terraform.tfstate"))
cloud = {sg["GroupId"]: sg for sg in
         json.load(open(sys.argv[1]))["SecurityGroups"]}
drifted = False
for res in state["resources"]:
    if res["type"] != "aws_security_group":
        continue
    attrs = res["instances"][0]["attributes"]
    perms = cloud[attrs["id"]]["IpPermissions"]
    want = {(r["protocol"], r["from_port"], r["to_port"], c)
            for r in attrs["ingress"] for c in r["cidr_blocks"]}
    have = {(p["IpProtocol"], p["FromPort"], p["ToPort"], ip["CidrIp"])
            for p in perms for ip in p["IpRanges"]}
    for sign, rules in (("+", have - want), ("-", want - have)):
        for rule in sorted(rules):
            print(f"{sign} aws_security_group.{res['name']} ingress {rule}")
    drifted |= want != have
print(f"state serial {state['serial']}: {'drift' if drifted else 'no drift'}")
sys.exit(2 if drifted else 0)
