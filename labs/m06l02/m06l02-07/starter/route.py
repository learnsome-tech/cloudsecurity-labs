import json

def test(rule, value):
    if isinstance(rule, dict) and "numeric" in rule:
        op, limit = rule["numeric"]
        return isinstance(value, (int, float)) and op == ">=" and value >= limit
    return rule == value

def matches(pattern, event):
    for field, rule in pattern.items():
        value = event.get(field)
        if isinstance(rule, dict):
            if not isinstance(value, dict) or not matches(rule, value):
                return False
        elif not any(test(r, value) for r in rule):
            return False
    return True

pattern = json.load(open("high-severity.json"))
for event in json.load(open("events.json")):
    target = "page" if matches(pattern, event) else "queue"
    print(target.ljust(5), event["detail"]["severity"], event["detail"]["type"])
