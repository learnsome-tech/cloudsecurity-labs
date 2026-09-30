import json
from statement import applies

def load(*names):
    return [json.load(open(f"scp/{n}.json")) for n in names]

def statements(policies):
    return [s for p in policies for s in p["Statement"]]

def decide(levels, req):
    for level, policies in levels.items():       # 1. any Deny, anywhere
        for s in statements(policies):
            if s["Effect"] == "Deny" and applies(s, req):
                return f"denied by {s['Sid']} ({level})"
    for level, policies in levels.items():       # 2. an Allow at every level
        if not any(s["Effect"] == "Allow" and applies(s, req)
                   for s in statements(policies)):
            return f"no Allow at {level}"
    return "allowed; IAM policies decide next"
