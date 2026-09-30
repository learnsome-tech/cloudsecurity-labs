import fileinput, math, re, sys
from collections import Counter

RULE = re.compile(r"\b(exmp_[A-Za-z0-9]{32})\b")      # regex from the toml
ALLOW_PATH = re.compile(r"^tests/fixtures/")

def entropy(s):
    return sum(-c / len(s) * math.log2(c / len(s)) for c in Counter(s).values())

found, path, line = 0, "", 0
for raw in fileinput.input():                 # a file argument, or stdin
    if raw.startswith("+++ "):
        path = raw[6:].strip()                # "+++ b/app/client.py"
    elif raw.startswith("@@"):
        line = int(re.search(r"\+(\d+)", raw)[1])
    elif raw.startswith("+"):
        m = RULE.search(raw) if "exmp_" in raw.lower() else None
        if m and entropy(m[1]) > 3.5 and not ALLOW_PATH.match(path):
            found += 1
            print(f"{path}:{line} exampleorg-api-token {m[1][:9]}...REDACTED")
        line += 1
sys.exit(1 if found else 0)
