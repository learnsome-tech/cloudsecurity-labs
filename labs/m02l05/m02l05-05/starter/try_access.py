from harness import get, start
from idp import b64, issue, unb64

base = start()  # the broker on 127.0.0.1, on a port the OS picks
alice = issue("alice@example.com", ["payroll-admins"], iat=1789999000)
bob = issue("bob@example.com", ["engineering"], iat=1789999000)
head, body, sig = bob.split(".")
promoted = unb64(body).replace(b'"engineering"', b'"payroll-admins"')
forged = f"{head}.{b64(promoted)}.{sig}"

for label, token, device in [
        ("alice, company laptop", alice, "LAPTOP-0142"),
        ("alice, personal tablet", alice, "TABLET-7731"),
        ("bob, company laptop", bob, "LAPTOP-0187"),
        ("bob, edited groups", forged, "LAPTOP-0187"),
        ("no token", "", "LAPTOP-0142")]:
    status, text = get(base, token, device)
    print(f"{label:23} {status} {text}")
