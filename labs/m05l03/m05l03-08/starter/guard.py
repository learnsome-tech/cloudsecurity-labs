import json, sys

def deny(plan):                                   # mirrors guardrails.rego
    for rc in plan["resource_changes"]:
        c, addr = rc["change"], rc["address"]
        after, before = c["after"] or {}, c["before"] or {}
        label = (after.get("tags") or {}).get("data_classification")
        was = (before.get("tags") or {}).get("data_classification")
        if c["actions"] != ["delete"] and not label:
            yield f"{addr}: no data_classification tag"
        if label in ("confidential", "restricted") and not (
                after.get("storage_encrypted") or after.get("encrypted")):
            yield f"{addr}: sensitive data not encrypted at rest"
        if "delete" in c["actions"] and was == "restricted":
            yield f"{addr}: plan destroys restricted data"

plan = json.load(open(sys.argv[1]))
msgs = sorted(set(deny(plan)))
for m in msgs:
    print(m)
print(f"{len(msgs)} violation(s) in {len(plan['resource_changes'])} changes")
sys.exit(1 if msgs else 0)
