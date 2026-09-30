import ipaddress, json

ADMIN_PORTS = (22, 3389)

def admin_ports_open_to_world(ci):
    for perm in ci["configuration"]["ipPermissions"]:
        cidrs = [r["cidrIp"] for r in perm["ipv4Ranges"]]
        cidrs += [r["cidrIpv6"] for r in perm["ipv6Ranges"]]
        world = [c for c in cidrs if ipaddress.ip_network(c).prefixlen == 0]
        for port in ADMIN_PORTS:
            if world and (perm["ipProtocol"] == "-1"
                          or perm["fromPort"] <= port <= perm["toPort"]):
                yield f"port {port} open to {world[0]}"

def public_access_not_blocked(ci):
    block = ci["supplementaryConfiguration"]["PublicAccessBlockConfiguration"]
    yield from (f"{name} is off" for name, on in block.items() if not on)

CONTROLS = {"AWS::EC2::SecurityGroup": admin_ports_open_to_world,
            "AWS::S3::Bucket": public_access_not_blocked}
ITEMS = json.load(open("config-items.json"))["configurationItems"]
