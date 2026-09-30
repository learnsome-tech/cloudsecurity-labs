import json
from pss import violations

for path in ("web-pod.json", "hardened-pod.json", "log-agent.json"):
    pod = json.load(open(path))
    for level in ("baseline", "restricted"):
        bad = violations(pod, level)
        print(f"{path} at {level}:", "forbidden" if bad else "allowed")
        for problem in bad:
            print("  " + problem)
        if bad:
            break  # restricted includes every baseline check
