# Cloud Security & DevSecOps Engineering — lesson m03l03 — Static Application Security Testing with Semgrep
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l03
# © LearnSome.tech
import csv, json, pathlib

inventory = {row["repo"]: row for row in csv.DictReader(open("inventory.csv"))}
scans = {p.stem: json.loads(p.read_text())
         for p in pathlib.Path("scans").glob("*.json")}

for repo in sorted(inventory.keys() | scans.keys()):
    asset, scan = inventory.get(repo), scans.get(repo)
    if asset is None:
        print(f"{repo}: scanned but not in the inventory, nobody owns it")
    elif asset["status"] == "decommissioned":
        if scan:
            print(f"{repo}: decommissioned but still building")
    elif scan is None:
        print(f"{repo}: active and never scanned, ask {asset['owner']}")
    else:
        levels = [r["extra"]["severity"] for r in scan["results"]]
        print(f"{repo}: {levels.count('ERROR')} error(s) for {asset['owner']}, "
              f"data is {asset['classification']}")
