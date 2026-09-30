from fnmatch import fnmatchcase

OPS = {"StringEquals": (False, False), "StringNotEquals": (False, True),
       "StringLike": (True, False), "StringNotLike": (True, True),
       "ArnLike": (True, False), "ArnNotLike": (True, True)}

def as_list(value):
    return [value] if isinstance(value, str) else value

def holds(op, key, wanted, req):
    wildcard, negated = OPS[op]        # KeyError: an operator we do not model
    hit = any(fnmatchcase(req[key], w) if wildcard else req[key] == w
              for w in as_list(wanted))
    return hit != negated

def applies(stmt, req):
    names = as_list(stmt.get("Action") or stmt["NotAction"])
    hit = any(fnmatchcase(req["action"].lower(), n.lower()) for n in names)
    return (hit != ("NotAction" in stmt)) and all(
        holds(op, key, wanted, req)
        for op, pairs in stmt.get("Condition", {}).items()
        for key, wanted in pairs.items())
