import json, sys
from datetime import date

TODAY = date(2026, 9, 27)          # fixed, so the output never drifts
BLOCK = {"HIGH", "CRITICAL"}       # like --severity HIGH,CRITICAL --exit-code 1
rules = [l.split() for l in open(".trivyignore") if l.strip() and l[0] != "#"]
expiry = {r[0]: date.fromisoformat(r[1][4:]) if r[1:] else date.max
          for r in rules}

blocking = 0
for result in json.load(open(sys.argv[1]))["Results"]:
    for vuln in result.get("Vulnerabilities", []):
        vid, sev = vuln["VulnerabilityID"], vuln["Severity"]
        waived = expiry.get(vid, date.min) >= TODAY
        stop = sev in BLOCK and not waived
        blocking += stop
        note = "blocking" if stop else "waived" if waived else "reported"
        if vid in expiry and not waived:
            note += f" (waiver expired {expiry[vid]})"
        print(vuln["PkgName"], vuln["InstalledVersion"], vid, f"{sev}: {note}")
print(f"{blocking} blocking finding(s)")
sys.exit(1 if blocking else 0)
