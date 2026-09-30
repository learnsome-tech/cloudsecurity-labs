import json
from collections import Counter
from pss import violations

# saved from: kubectl get pods -n shop -o json > pods.json
pods = json.load(open("pods.json"))["items"]
tally = Counter()
for pod in pods:
    base = violations(pod, "baseline")
    strict = violations(pod, "restricted")
    tally.update(problem.split(" (")[0] for problem in strict)
    name = pod["metadata"]["name"]
    print(f"{name:<24} baseline {len(base)}   restricted {len(strict)}")
print("checks to fix before enforce=restricted:")
for check, count in tally.most_common():
    print(f"  {count} x {check}")
