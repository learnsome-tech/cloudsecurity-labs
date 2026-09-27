# Cloud Security & DevSecOps Engineering — lesson m04l04 — Runtime Anomaly Detection with Falco & eBPF
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m04l04
# © LearnSome.tech
import json
from collections import defaultdict

def behaviour(e):
    if e["evt.type"] == "execve":
        return "exec " + e["proc.exepath"]
    return f"connect {e['fd.sip']}:{e['fd.sport']}"

normal = defaultdict(set)  # image -> everything it did while learning
for e in map(json.loads, open("learn.jsonl")):
    normal[e["container.image.repository"]].add(behaviour(e))
for image, seen in normal.items():
    print(f"learned {len(seen)} behaviours for {image}")

for e in map(json.loads, open("watch.jsonl")):
    image, act = e["container.image.repository"], behaviour(e)
    if e.get("proc.is_exe_upper_layer"):
        print(e["evt.time"], "drift: binary not in the image:", act)
    elif act not in normal[image]:
        print(e["evt.time"], "new:", act)
