import hashlib, json, pathlib, subprocess

def openssl(*args):
    return subprocess.run(["openssl", *args], capture_output=True).returncode

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def sign_digest(folder):
    logs = sorted(pathlib.Path(folder).glob("*.json"))
    digest = {"digestEndTime": "2026-09-27T10:00:00Z", "logFiles": [
        {"s3Object": p.name, "hashValue": sha256(p)} for p in logs]}
    pathlib.Path("digest.json").write_text(json.dumps(digest, indent=2))
    openssl("genpkey", "-algorithm", "RSA", "-out", "trail.key")
    openssl("pkey", "-in", "trail.key", "-pubout", "-out", "trail.pub")
    openssl("dgst", "-sha256", "-sign", "trail.key",
            "-out", "digest.sig", "digest.json")
    return digest

if __name__ == "__main__":
    for entry in sign_digest("logs")["logFiles"]:
        print(entry["s3Object"][-24:], entry["hashValue"][:32])
