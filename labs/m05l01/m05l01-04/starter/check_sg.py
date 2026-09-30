import ipaddress, json, sys

def exposes_ssh(rule):
    ports = rule["from_port"] <= 22 <= rule["to_port"]
    if rule["protocol"] == "-1":
        ports = True
    nets = rule.get("cidr_blocks", []) + rule.get("ipv6_cidr_blocks", [])
    anyone = any(ipaddress.ip_network(n).prefixlen == 0 for n in nets)
    return ports and anyone

tf = json.load(open(sys.argv[1]))
failed = 0
for name, sg in tf["resource"]["aws_security_group"].items():
    bad = [r for r in sg["ingress"] if exposes_ssh(r)]
    failed += bool(bad)
    result = "FAILED" if bad else "PASSED"
    print(f"CKV_AWS_24 {result} aws_security_group.{name}")
    for r in bad:
        print(f"  {r['description']}: ports {r['from_port']}-{r['to_port']}")
sys.exit(1 if failed else 0)
