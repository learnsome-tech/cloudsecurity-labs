import json
from issuer import b64, mint, unb64
from sts import validate

good = mint("repo:example-org/payments-api:environment:production")
head, body, sig = good.split(".")
print(json.loads(unb64(head)))
for name, value in json.loads(unb64(body)).items():
    print(f"  {name:4} {value}")

forged = b64(unb64(body).replace(b"payments", b"billing"))
tests = {"genuine": good, "edited sub": f"{head}.{forged}.{sig}",
         "other audience": mint("x", aud="https://github.com/example-org"),
         "expired": mint("x", exp=1789999800)}
for label, token in tests.items():
    print(f"{label:15} {validate(token)}")
