# Cloud Security & DevSecOps Engineering — lesson m01l04 — Security Landing Zones & Centralized Egress Inspection
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m01l04
# © LearnSome.tech
import re
from glob import glob

RULES = """kube-apiserver anonymous-auth     false
kube-apiserver authorization-mode RBAC
kube-apiserver profiling          false
kube-apiserver token-auth-file    -
etcd           client-cert-auth   true
kubelet        anonymous-auth     false
kubelet        read-only-port     0"""

def flags(path):                        # every --name=value on a command line
    return dict(re.findall(r"--([\w-]+)=([^\s\"]+)", open(path).read()))

for rule in RULES.splitlines():
    part, flag, wanted = rule.split()
    row = f"{rule:41}"
    for node in ("before", "after"):
        value = flags(glob(f"{node}/{part}.*")[0]).get(flag, "-")
        row += f"{value:13}{'ok' if wanted in value.split(',') else 'fail':5}"
    print(row)
