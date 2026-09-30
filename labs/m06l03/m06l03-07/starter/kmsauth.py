import fnmatch, json
ROOT = "arn:aws:iam::111122223333:root"
KEY = json.load(open("key-policy.json"))["Statement"]
IAM = json.load(open("iam-policies.json"))
def effects(statements, principal, action, context):
    return {s["Effect"] for s in statements
            if s.get("Principal", {}).get("AWS", principal) == principal
            and any(fnmatch.fnmatchcase(action, a) for a in s["Action"])
            and all(context.get(k) == v for k, v in
                    s.get("Condition", {}).get("StringEquals", {}).items())}

def decide(role, action, context):
    key = effects(KEY, role, action, context)
    root = effects(KEY, ROOT, action, context)
    iam = effects(IAM.get(role, []), role, action, context)
    if "Deny" in key | root | iam:
        return "explicit deny"
    if "Allow" in key:
        return "allow (key policy)"
    if "Allow" in root and "Allow" in iam:
        return "allow (IAM, trusted by key policy)"
    return "implicit deny"
