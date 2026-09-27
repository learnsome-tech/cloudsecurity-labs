# Cloud Security & DevSecOps Engineering — lesson m04l01 — Container Hardening: Distroless & Rootless
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m04l01
# © LearnSome.tech
import textwrap
CAPS = ["CHOWN", "DAC_OVERRIDE", "DAC_READ_SEARCH", "FOWNER", "FSETID",
        "KILL", "SETGID", "SETUID", "SETPCAP", "LINUX_IMMUTABLE",
        "NET_BIND_SERVICE", "NET_BROADCAST", "NET_ADMIN", "NET_RAW",
        "IPC_LOCK", "IPC_OWNER", "SYS_MODULE", "SYS_RAWIO", "SYS_CHROOT",
        "SYS_PTRACE", "SYS_PACCT", "SYS_ADMIN", "SYS_BOOT", "SYS_NICE",
        "SYS_RESOURCE", "SYS_TIME", "SYS_TTY_CONFIG", "MKNOD", "LEASE",
        "AUDIT_WRITE", "AUDIT_CONTROL", "SETFCAP"]

def decode(mask):
    bits = int(mask, 16)
    return [name for n, name in enumerate(CAPS) if bits >> n & 1]

for path in ("root.status", "nonroot.status", "hardened.status"):
    f = dict(line.split(":\t", 1) for line in open(path))
    eff, bnd = decode(f["CapEff"]), decode(f["CapBnd"])
    uid, nnp = f["Uid"].split()[0], f["NoNewPrivs"].strip()
    print(f"{path}: uid {uid}, NoNewPrivs {nnp}, "
          f"bounding {len(bnd)}, effective {len(eff)}")
    if eff:
        print(textwrap.fill(" ".join(eff), 72, initial_indent="  ",
                            subsequent_indent="  "))
