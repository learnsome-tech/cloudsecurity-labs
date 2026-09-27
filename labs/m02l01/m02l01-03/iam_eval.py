# Cloud Security & DevSecOps Engineering — lesson m02l01 — Cloud IAM Architecture & Permission Boundaries
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l01
# © LearnSome.tech
from fnmatch import fnmatchcase as glob
TESTS = {"StringEquals": str.__eq__, "Bool": str.__eq__, "StringLike": glob}

def many(value):
    return [value] if isinstance(value, str) else value

def holds(op, key, wants, ctx):
    test = TESTS[op]
    return key in ctx and any(test(ctx[key], w) for w in many(wants))

def matches(st, action, resource, ctx):
    return (any(glob(action.lower(), a.lower()) for a in many(st["Action"]))
            and any(glob(resource, r) for r in many(st["Resource"]))
            and all(holds(op, k, v, ctx) for op, kv in
                    st.get("Condition", {}).items() for k, v in kv.items()))

def decide(policy, action, resource, ctx):
    hits = {s["Effect"] for s in policy["Statement"]
            if matches(s, action, resource, ctx)}
    if "Deny" in hits:
        return "explicit deny"
    return "allow" if "Allow" in hits else "implicit deny"
