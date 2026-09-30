import json
from ipaddress import ip_network

ADMIN = {22: "ssh", 3306: "mysql", 3389: "rdp", 5432: "postgres"}
INTERNAL = [ip_network(n) for n in
            ("10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16", "fc00::/7")]

def internal(net):
    return any(net.version == i.version and net.subnet_of(i) for i in INTERNAL)
def ports(rule):
    if rule["IpProtocol"] == "-1": return list(ADMIN)     # all ports
    tcp = rule["IpProtocol"] in ("tcp", "6")
    return [p for p in ADMIN if tcp and rule["FromPort"] <= p <= rule["ToPort"]]

for g in json.load(open("sg.json"))["SecurityGroups"]:
    for rule in g["IpPermissions"]:
        exposed = ", ".join(ADMIN[p] for p in ports(rule))
        cidrs = [r.get("CidrIp") or r["CidrIpv6"]
                 for r in rule["IpRanges"] + rule["Ipv6Ranges"]]
        for net in map(ip_network, cidrs):
            if exposed and not internal(net):
                print(f"{g['GroupName']:13} {str(net):10} reaches {exposed}")
