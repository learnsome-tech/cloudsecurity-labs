# Cloud Security & DevSecOps Engineering — lesson m06l01 — CloudTrail Logging, Integrity Validation & Athena
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m06l01
# © LearnSome.tech
import json, pathlib
from digest import openssl, sha256, sign_digest

def validate(when):
    ok = openssl("dgst", "-sha256", "-verify", "trail.pub",
                 "-signature", "digest.sig", "digest.json") == 0
    files = json.loads(pathlib.Path("digest.json").read_text())["logFiles"]
    bad = [f["s3Object"][-9:] for f in files
           if sha256(pathlib.Path("logs", f["s3Object"])) != f["hashValue"]]
    print(f"{when}: signature {'valid' if ok else 'invalid'}, changed {bad}")

sign_digest("logs")
validate("as delivered")
log = sorted(pathlib.Path("logs").glob("*.json"))[1]
records = json.loads(log.read_text())["Records"]
kept = [r for r in records if r["eventName"] != "StopLogging"]
log.write_text(json.dumps({"Records": kept}))
validate("record deleted")
digest = json.loads(pathlib.Path("digest.json").read_text())
digest["logFiles"][1]["hashValue"] = sha256(log)
pathlib.Path("digest.json").write_text(json.dumps(digest, indent=2))
validate("digest rewritten")
