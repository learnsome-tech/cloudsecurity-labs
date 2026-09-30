import json, sys
from collections import Counter

def findings(path):
    for run in json.load(open(path))["runs"]:
        for r in run.get("results", []):
            loc = r["locations"][0]["physicalLocation"]
            yield (r["ruleId"], loc["artifactLocation"]["uri"],
                   loc["region"]["startLine"], r.get("level", "warning"))

base, head = sys.argv[1], sys.argv[2]
known = Counter((rule, uri) for rule, uri, _, _ in findings(base))
blocking = 0
for rule, uri, line, level in findings(head):
    state = "existing" if known[(rule, uri)] > 0 else "new"
    known[(rule, uri)] -= 1
    stop = state == "new" and level == "error"
    blocking += stop
    print(f"{state:9}{level:8}{rule.split('.')[-1]:24}{uri}:{line}")
print(f"gate: {blocking} new error(s),", "merge blocked" if blocking else "ok")
sys.exit(1 if blocking else 0)
