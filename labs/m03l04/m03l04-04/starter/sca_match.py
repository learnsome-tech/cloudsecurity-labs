import json, pathlib, re

def v(text):                     # "1.26.15" -> (1, 26, 15): plain releases only
    return tuple(int(part) for part in text.split("."))

def fix_for(version, events):    # OSV events come in introduced, fixed pairs
    for intro, fixed in zip(events[::2], events[1::2]):
        if v(intro["introduced"]) <= v(version) < v(fixed["fixed"]):
            return fixed["fixed"]

lock = open("requirements.txt").read()
pins = dict(re.findall(r"^([\w.-]+)==([\d.]+)", lock, re.M))
for path in sorted(pathlib.Path("advisories").glob("*.json")):
    adv = json.loads(path.read_text())
    for hit in adv["affected"]:
        name = hit["package"]["name"]
        events = hit["ranges"][0]["events"]
        if name in pins and (fix := fix_for(pins[name], events)):
            print(f"{name} {pins[name]}  {adv['aliases'][0]}  "
                  f"{adv['database_specific']['severity']}  fixed in {fix}")
