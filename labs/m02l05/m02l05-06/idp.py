# Cloud Security & DevSecOps Engineering — lesson m02l05 — Zero-Trust Network Access & IdP Federation
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l05
# © LearnSome.tech
"""Stand-in identity provider: signs HS256 ID tokens with a shared key."""
import base64, hashlib, hmac, json, secrets

KEY = secrets.token_bytes(32)  # shared with the broker, never printed
AUDIENCE = "payroll.example.com"


def b64(raw):
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


def unb64(text):
    return base64.urlsafe_b64decode(text + "=" * (-len(text) % 4))


def sign(signing_input):
    return b64(hmac.new(KEY, signing_input.encode(), hashlib.sha256).digest())


def issue(sub, groups, iat):
    head = b64(json.dumps({"alg": "HS256", "typ": "JWT"}).encode())
    body = b64(json.dumps({"iss": "https://idp.example.com", "aud": AUDIENCE,
                           "sub": sub, "groups": groups,
                           "iat": iat, "exp": iat + 3600}).encode())
    return f"{head}.{body}.{sign(head + '.' + body)}"


def verify(token, now):
    parts = token.split(".")
    if len(parts) != 3:
        raise ValueError("no token")
    head, body, sig = parts
    if not hmac.compare_digest(sig, sign(head + "." + body)):
        raise ValueError("bad signature")
    claims = json.loads(unb64(body))
    if claims["aud"] != AUDIENCE:
        raise ValueError("token is for another app")
    if claims["exp"] <= now:
        raise ValueError("token expired")
    return claims
