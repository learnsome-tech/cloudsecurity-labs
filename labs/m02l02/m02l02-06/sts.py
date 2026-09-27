# Cloud Security & DevSecOps Engineering — lesson m02l02 — Workload Identity Federation: Eliminating Static Keys
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l02
# © LearnSome.tech
import json
from subprocess import run
from issuer import ISS, PUB, unb64

def validate(token, now=1789999900):  # pinned clock so the output repeats
    head, body, sig = token.split(".")
    open("sig.bin", "wb").write(unb64(sig))
    verify = run(["openssl", "dgst", "-sha256", "-verify", PUB,
                  "-signature", "sig.bin"], capture_output=True,
                 input=f"{head}.{body}".encode())
    claims = json.loads(unb64(body))
    checks = {"signature": verify.returncode == 0,
              "issuer": claims["iss"] == ISS,
              "audience": claims["aud"] == "sts.amazonaws.com",
              "expiry": claims["exp"] > now}
    failed = [name for name, ok in checks.items() if not ok]
    return "rejected: " + ", ".join(failed) if failed else "accepted"
