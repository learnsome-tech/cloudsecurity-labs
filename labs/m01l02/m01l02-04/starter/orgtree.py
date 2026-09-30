import json

org = json.load(open("org.json"))
root = org["Root"]["Id"]
nodes = org["OrganizationalUnits"] + org["Accounts"]
parent = {n["Id"]: n["ParentId"] for n in nodes}
name = {n["Id"]: n["Name"] for n in nodes} | {root: "Root"}

def ancestors(node):                    # root first, direct parent last
    chain = []
    while node != root:
        node = parent[node]
        chain.insert(0, node)
    return chain

for acct in org["Accounts"]:
    chain = ancestors(acct["Id"])
    note = ("management account: SCPs never apply here"
            if acct["Id"] == org["MasterAccountId"] else
            "no OU: OU policies skip it" if len(chain) == 1 else "")
    print(f"{acct['Name']:17} {'/'.join(name[i] for i in chain):20} {note}")
