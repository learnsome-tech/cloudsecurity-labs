import base64, json
from subprocess import run

KEY, PUB = "issuer-key.pem", "issuer-public.pem"  # throwaway demo key pair
run(["openssl", "genpkey", "-algorithm", "RSA", "-quiet", "-out", KEY])
run(["openssl", "pkey", "-in", KEY, "-pubout", "-out", PUB])
ISS = "https://token.actions.githubusercontent.com"

def b64(raw):
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()

def unb64(text):
    return base64.urlsafe_b64decode(text + "=" * (-len(text) % 4))

def mint(sub, aud="sts.amazonaws.com", exp=1790000000):
    header = {"alg": "RS256", "typ": "JWT", "kid": "demo-key"}
    claims = {"iss": ISS, "aud": aud, "sub": sub, "iat": exp - 300,
              "exp": exp}
    body = ".".join(b64(json.dumps(p).encode()) for p in (header, claims))
    sig = run(["openssl", "dgst", "-sha256", "-sign", KEY],
              input=body.encode(), capture_output=True).stdout
    return body + "." + b64(sig)
