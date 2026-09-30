import subprocess

# A Secret as the API server hands it to storage (JSON here for clarity)
secret = b'{"kind":"Secret","data":{"password":"ZXhhbXBsZS1vbmx5"}}'
key = bytes(range(32))  # demo key; a real one is 32 bytes from /dev/urandom
iv = bytes(range(16))   # fixed so the output repeats; the real IV is random
prefix = b"k8s:enc:aescbc:v1:key1:"

def aes_cbc(data, *extra):
    cmd = ["openssl", "enc", "-aes-256-cbc", *extra,
           "-K", key.hex(), "-iv", iv.hex()]
    return subprocess.run(cmd, input=data, capture_output=True).stdout

stored = {"identity": secret, "aescbc": prefix + iv + aes_cbc(secret)}
for provider, value in stored.items():
    readable = b"ZXhhbXBsZS1vbmx5" in value
    print(f"{provider}: {len(value)} bytes, password readable: {readable}")
    print(" ", "".join(chr(c) if 32 <= c < 127 else "." for c in value[:60]))

body = stored["aescbc"][len(prefix) + 16:]
print("decrypted with key1:", aes_cbc(body, "-d")[:36])
