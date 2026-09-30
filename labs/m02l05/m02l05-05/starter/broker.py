import json
from idp import verify

POLICY = {"groups": {"payroll-admins", "finance"},
          "device": {"managed": True, "disk_encrypted": True}}
USERS = json.load(open("directory.json"))  # kept current by SCIM
DEVICES = json.load(open("devices.json"))  # posture from device management

def decide(headers, now):
    token = headers.get("Authorization", "").removeprefix("Bearer ")
    try:
        claims = verify(token, now)
    except ValueError as reason:
        return 401, f"sign in again: {reason}"
    if not USERS.get(claims["sub"], {}).get("active"):
        return 403, "account is disabled in the directory"
    if not POLICY["groups"] & set(claims["groups"]):
        return 403, "no group of yours grants this app"
    device = DEVICES.get(headers.get("X-Device-Id", ""), {})
    if failed := [k for k, v in POLICY["device"].items() if device.get(k) != v]:
        return 403, "device fails posture: " + ", ".join(failed)
    return 200, f"payroll for {claims['sub']}"
