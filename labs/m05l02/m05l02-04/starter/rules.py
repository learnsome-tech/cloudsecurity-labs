import json

def allow(i):                                  # default allow := false
    rule_one = i["user"].get("team") == "platform"
    rule_two = (i["action"] == "read"
                and i["bucket"]["owner"] == i["user"].get("team"))
    return rule_one or rule_two                # same name: bodies ORed

def deny(i):                                   # deny contains msg
    msgs = set()
    if i["action"] == "delete" and not i["user"].get("mfa"):
        msgs.add(f"{i['user']['name']}: delete without MFA")
    return sorted(msgs)

if __name__ == "__main__":
    for i in json.load(open("inputs.json")):
        who = f"{i['user']['name']} {i['action']} {i['bucket']['name']}"
        print(f"{who}: allow={allow(i)} deny={deny(i)}")
