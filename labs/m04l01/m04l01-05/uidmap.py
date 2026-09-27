# Cloud Security & DevSecOps Engineering — lesson m04l01 — Container Hardening: Distroless & Rootless
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m04l01
# © LearnSome.tech
def load(path):
    # each line: first uid inside, first uid outside, length of the range
    return [tuple(map(int, line.split())) for line in open(path)]

def to_host(uid, ranges):
    for inside, outside, count in ranges:
        if inside <= uid < inside + count:
            return outside + (uid - inside)
    return None

for path in ("no-userns.uid_map", "userns.uid_map"):
    ranges = load(path)
    for uid in (0, 65532, 70000):
        host = to_host(uid, ranges)
        where = "not mapped" if host is None else f"host uid {host}"
        print(f"{path}: container uid {uid:>5} is {where}")
