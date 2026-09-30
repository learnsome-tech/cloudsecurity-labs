def selects(sel, have):
    return all(have.get(k) == v for k, v in sel.get("matchLabels", {}).items())

def peer_ok(peer, policy_ns, other):  # ipBlock peers are not modelled here
    ns_ok = (selects(peer["namespaceSelector"], other["ns_labels"])
             if "namespaceSelector" in peer else other["ns"] == policy_ns)
    return ns_ok and selects(peer.get("podSelector", {}), other["labels"])

def allowed(policies, pod, other, port, direction):
    mine = [p for p in policies if p["metadata"]["namespace"] == pod["ns"]
            and selects(p["spec"]["podSelector"], pod["labels"])
            and direction in p["spec"]["policyTypes"]]
    if not mine:
        return True  # no policy selects this pod, so it is not isolated
    for rule in (r for p in mine for r in p["spec"].get(direction.lower(), [])):
        peers = rule.get("from" if direction == "Ingress" else "to")
        ports = rule.get("ports")  # a missing or empty list means any
        if (not peers or any(peer_ok(x, pod["ns"], other) for x in peers)) \
                and (not ports or any(p["port"] == port for p in ports)):
            return True
    return False
