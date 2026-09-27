# Cloud Security & DevSecOps Engineering — lesson m02l04 — Least Privilege Enforcement & CIEM Architecture
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l04
# © LearnSome.tech
import json
from fnmatch import fnmatchcase
from iam_eval import many
from trail import calls

policy = json.load(open("reporting-role.json"))
catalogue = json.load(open("actions.json"))  # a subset of the real list
used = {action for action, _ in calls("trail-90d.json", "reporting-app")}
granted = {a for st in policy["Statement"] for p in many(st["Action"])
           for a in catalogue if fnmatchcase(a.lower(), p.lower())}

print(f"granted {len(granted)}, used {len(used)}, unused {len(granted - used)}")
danger = ("Delete", "Purge", "Schedule", "Disable", "PutBucket", "PutKey")
for service in sorted({a.split(":")[0] for a in granted}):
    unused = [a.split(":")[1] for a in sorted(granted - used)
              if a.startswith(service + ":")]
    worst = [name for name in unused if name.startswith(danger)]
    print(f"{service:8} {len(unused):2} unused; destructive: {' '.join(worst)}")
