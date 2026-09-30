import re
text = open("kube-apiserver.yaml").read()
flags = dict(re.findall(r"^\s*- --([\w-]+)=(.*)$", text, re.MULTILINE))
modes = flags.get("authorization-mode", "").split(",")
plugins = flags.get("enable-admission-plugins", "").split(",")

checks = {  # an absent flag means the API server's built-in default
    "anonymous-auth=false": flags.get("anonymous-auth") == "false",
    "authorization-mode has Node and RBAC": {"Node", "RBAC"} <= set(modes),
    "authorization-mode has no AlwaysAllow": "AlwaysAllow" not in modes,
    "NodeRestriction admission plugin": "NodeRestriction" in plugins,
    "profiling=false": flags.get("profiling") == "false",
    "audit-log-path set": "audit-log-path" in flags,
    "encryption-provider-config set": "encryption-provider-config" in flags,
    "kubelet CA set": "kubelet-certificate-authority" in flags,
}
for name, ok in checks.items():
    print("pass" if ok else "fail", name)
print(sum(not ok for ok in checks.values()), "of", len(checks), "checks fail")
