# Cloud Security & DevSecOps Engineering — lesson m01l05 — Cloud Network Isolation: VPC Peering & PrivateLink
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m01l05
# © LearnSome.tech
import json
from ipaddress import ip_address, ip_network

tables = {t["VpcId"]: t["Routes"]
          for t in json.load(open("routes.json"))["RouteTables"]}
PEERS = {"pcx-1a": {"vpc-app", "vpc-hub"}, "pcx-2b": {"vpc-hub", "vpc-data"}}

def lookup(vpc, dst):                   # the most specific matching route wins
    routes = [(ip_network(r["DestinationCidrBlock"]), r) for r in tables[vpc]]
    hits = [(net.prefixlen, r) for net, r in routes if dst in net]
    return max(hits, key=lambda h: h[0])[1] if hits else None
def trace(vpc, dst, via=None):
    route = lookup(vpc, ip_address(dst))
    local = route is not None and route.get("GatewayId") == "local"
    if local or route is None or via:     # peering is not transitive
        return [vpc, "delivered" if local else "dropped"]
    pcx = route["VpcPeeringConnectionId"]
    return [vpc] + trace((PEERS[pcx] - {vpc}).pop(), dst, via=pcx)

for src, dst in [("vpc-app", "10.2.4.20"), ("vpc-app", "10.3.9.15"),
                 ("vpc-hub", "10.3.9.15")]:
    print(f"{src} to {dst}: {' > '.join(trace(src, dst))}")
