# Cloud Security & DevSecOps Engineering — lesson m05l04 — Continuous IaC Drift Detection & State Protection
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m05l04
# © LearnSome.tech
import json

state = json.load(open("terraform.tfstate"))
print(f"lineage {state['lineage']}, serial {state['serial']}")
secrets = set()
for res in state["resources"]:
    for inst in res["instances"]:
        for path in inst["sensitive_attributes"]:
            name = path[0]["value"]
            value = inst["attributes"][name]
            secrets.add(value)
            print(f"{res['type']}.{res['name']}.{name}: marked sensitive,"
                  f" {len(value)} characters in plain text")
for name, out in state["outputs"].items():
    leaked = any(s in out["value"] for s in secrets)
    label = "marked sensitive" if out.get("sensitive") else "not marked"
    print(f"output {name}: {label}, contains a secret: {leaked}")
