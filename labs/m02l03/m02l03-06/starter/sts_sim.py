import json
from iam_eval import decide, many, matches
ROLES = {r["Role"]["Arn"]: r["Role"] for r in json.load(open("roles.json"))}

def principals(session):  # arn:aws:sts::ACCOUNT:assumed-role/ROLE/NAME
    account, role = session.split(":")[4], session.split("/")[1]
    return {f"arn:aws:iam::{account}:role/{role}",
            f"arn:aws:iam::{account}:root"}

def assume_role(session, policy, arn, name, seconds=3600, ctx={}):
    if decide(policy, "sts:AssumeRole", arn, ctx) != "allow":
        return "AccessDenied: the caller's own policy does not allow it"
    trust = ROLES[arn]["AssumeRolePolicyDocument"]["Statement"]
    if not any(st["Effect"] == "Allow"
               and principals(session) & set(many(st["Principal"]["AWS"]))
               and matches({**st, "Resource": "*"}, "sts:AssumeRole", "*", ctx)
               for st in trust):
        return "AccessDenied: the role's trust policy does not match"
    if seconds > 3600:  # the caller is a role session, so this is chaining
        return "ValidationError: a chained session is limited to one hour"
    account, role = arn.split(":")[4], arn.split("/")[1]
    return f"arn:aws:sts::{account}:assumed-role/{role}/{name}"
