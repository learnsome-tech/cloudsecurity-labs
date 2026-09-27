# Cloud Security & DevSecOps Engineering — lesson m01l02 — AWS Organizations, Account Hierarchies & Azure Management Groups
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m01l02
# © LearnSome.tech
import json, re

org = json.load(open("org.json"))
parent = {n["Id"]: n["ParentId"]
          for n in org["OrganizationalUnits"] + org["Accounts"]}

def org_path(account_id):               # the aws:PrincipalOrgPaths value
    ids, node = [], account_id
    while node in parent:
        node = parent[node]
        ids.insert(0, node)
    return "/".join([org["OrganizationId"], *ids]) + "/"

def string_like(pattern, value):        # IAM StringLike: * and ? wildcards
    rx = re.escape(pattern).replace(r"\*", ".*").replace(r"\?", ".")
    return re.fullmatch(rx, value) is not None

POLICY = "o-a1b2c3d4e5/r-a1b2/ou-a1b2-wkld0001/*"
for a in org["Accounts"]:
    path = org_path(a["Id"])
    print(f"{a['Name']:17} {path:52} {string_like(POLICY, path)}")
