# Cloud Security & DevSecOps Engineering — lesson m04l04 — Runtime Anomaly Detection with Falco & eBPF
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m04l04
# © LearnSome.tech
import json, re

SHELLS = {"ash", "bash", "csh", "ksh", "sh", "tcsh", "zsh", "dash"}
WEB = {"nginx", "gunicorn", "uwsgi", "node", "java"}
TOKEN_DIR = "/var/run/secrets/kubernetes.io/serviceaccount"

RULES = [  # (priority, condition, output), hand-copied from the YAML
    ("Warning", lambda e: e["evt.type"] in ("execve", "execveat")
        and e["container.id"] != "host" and e["proc.name"] in SHELLS
        and e["proc.pname"] in WEB,
     "Shell under web server (parent=%proc.pname cmdline=%proc.cmdline "
     "pod=%k8s.pod.name)"),
    ("Error", lambda e: e["evt.type"] in ("open", "openat", "openat2")
        and e["container.id"] != "host" and e["proc.name"] not in WEB
        and e.get("fd.name", "").startswith(TOKEN_DIR),
     "Token read (proc=%proc.name file=%fd.name pod=%k8s.pod.name)"),
]
for e in map(json.loads, open("events.jsonl")):
    for priority, condition, output in RULES:
        if condition(e):
            text = re.sub(r"%([\w.]+)", lambda m: str(e[m[1]]), output)
            print(f"{e['evt.time']}: {priority} {text}")
