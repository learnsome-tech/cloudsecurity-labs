import json
from netpol import allowed

pods = json.load(open("pods.json"))
policies = json.load(open("shop-policies.json"))  # the YAML, as JSON

def connect(src, dst, port):
    out = allowed(policies, pods[src], pods[dst], port, "Egress")
    into = allowed(policies, pods[dst], pods[src], port, "Ingress")
    verdict = "allowed" if out and into else "blocked"
    print(f"{src:<8} -> {dst + ':' + str(port):<16} egress {out!s:<5} "
          f"ingress {into!s:<5} {verdict}")

connect("web", "api", 8080)
connect("web", "db", 5432)
connect("api", "db", 5432)
connect("api", "kube-dns", 53)
connect("db", "grafana", 3000)
connect("grafana", "web", 8080)
