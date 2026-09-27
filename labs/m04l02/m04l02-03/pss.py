# Cloud Security & DevSecOps Engineering — lesson m04l02 — Kubernetes Pod Security Standards: Baseline & Restricted
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m04l02
# © LearnSome.tech
HOST_NS = ("hostNetwork", "hostPID", "hostIPC")
SECCOMP_OK = ("RuntimeDefault", "Localhost")

def violations(pod, level):
    spec = pod["spec"]
    bad = [f"host namespaces ({k}=true)" for k in HOST_NS if spec.get(k)]
    bad += [f'hostPath volumes (volume "{v["name"]}")'
            for v in spec.get("volumes", []) if "hostPath" in v]
    for c in spec["containers"]:
        sc = spec.get("securityContext", {}) | c.get("securityContext", {})
        rules = {"privileged": not sc.get("privileged")}
        if level == "restricted":
            esc = sc.get("allowPrivilegeEscalation")
            drop = sc.get("capabilities", {}).get("drop", [])
            seccomp = sc.get("seccompProfile", {}).get("type")
            rules["allowPrivilegeEscalation != false"] = esc is False
            rules["unrestricted capabilities"] = "ALL" in drop
            rules["runAsNonRoot != true"] = sc.get("runAsNonRoot") is True
            rules["seccompProfile"] = seccomp in SECCOMP_OK
        bad += [f'{rule} (container "{c["name"]}")'
                for rule, ok in rules.items() if not ok]
    return bad
