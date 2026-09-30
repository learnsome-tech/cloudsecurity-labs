import json
from netpol import allowed

pods = json.load(open("pods.json"))
deny = json.load(open("default-deny.json"))
for variant in ("scrape-and.json", "scrape-or.json"):
    policies = [deny, json.load(open(variant))]
    for src in ("prometheus", "grafana", "debug-shell"):
        ok = allowed(policies, pods["api"], pods[src], 8081, "Ingress")
        where = pods[src]["ns"]
        print(f"{variant}: {src} in {where} -> api:8081",
              "allowed" if ok else "blocked")
