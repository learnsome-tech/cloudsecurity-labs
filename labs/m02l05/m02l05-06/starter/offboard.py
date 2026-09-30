import json
import urllib.request
from harness import get, send, start
from idp import issue

base = start()
alice = issue("alice@example.com", ["payroll-admins"], iat=1789999000)
print("before:", *get(base, alice, "LAPTOP-0142"))

patch = {"schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
         "Operations": [{"op": "replace", "path": "active", "value": False}]}
user = "2819c223-7f76-453a-919d-413861904646"
print("SCIM PATCH:", *send(urllib.request.Request(
    f"{base}/scim/v2/Users/{user}", method="PATCH",
    data=json.dumps(patch).encode(),
    headers={"Content-Type": "application/scim+json"})))

print("after: ", *get(base, alice, "LAPTOP-0142"))
exp = 1789999000 + 3600  # issued at, plus the hour the IdP allows
print(f"alice's token is still valid for {(exp - 1790000000) // 60} minutes")
