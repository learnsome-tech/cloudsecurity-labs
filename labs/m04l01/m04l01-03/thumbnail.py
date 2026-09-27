# Cloud Security & DevSecOps Engineering — lesson m04l01 — Container Hardening: Distroless & Rootless
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m04l01
# © LearnSome.tech
import subprocess
from pathlib import Path

# Two image filesystems: slim ships bin/sh, distroless does not.
Path("slim/bin").mkdir(parents=True, exist_ok=True)
Path("distroless/bin").mkdir(parents=True, exist_ok=True)
if not Path("slim/bin/sh").exists():
    Path("slim/bin/sh").symlink_to("/bin/sh")

def thumbnail(name, image):
    # the bug: user input pasted into a shell command
    cmd = f"echo resizing {name}"
    run = subprocess.run(cmd, shell=True, executable=f"{image}/bin/sh",
                         capture_output=True, text=True)
    return run.stdout.split("\n")[:-1]

payload = "cat.png; echo attacker command ran"
for image in ("slim", "distroless"):
    try:
        print(image, thumbnail(payload, image))
    except FileNotFoundError as err:
        print(image, "exec failed:", err.strerror, err.filename)
