# Cloud Security & DevSecOps Engineering — lesson m01l04 — Security Landing Zones & Centralized Egress Inspection
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m01l04
# © LearnSome.tech
import ssl
ALLOW = [".example.com", "pypi.org"]      # the rule group's Targets
def client_hello(host):                   # the first bytes a TLS client sends
    inc, out = ssl.MemoryBIO(), ssl.MemoryBIO()
    tls = ssl.create_default_context().wrap_bio(inc, out, server_hostname=host)
    try: tls.do_handshake()
    except ssl.SSLWantReadError: return out.read()   # no server will answer
def sni(hello):
    p = 44 + hello[43]                    # headers, version, random, session id
    p += 2 + int.from_bytes(hello[p:p + 2])          # cipher suites
    p += 1 + hello[p] + 2                 # compression, extensions length
    while hello[p:p + 2] != b"\x00\x00":  # extension type 0 is server_name
        p += 4 + int.from_bytes(hello[p + 2:p + 4])
    return hello[p + 9:p + 4 + int.from_bytes(hello[p + 2:p + 4])].decode()
def allowed(name):
    return any(name == t.lstrip(".") or (t[0] == "." and name.endswith(t))
               for t in ALLOW)

for host in ["updates.example.com", "example.com", "evilexample.com",
             "pypi.org", "paste.example.net"]:
    name = sni(client_hello(host))
    print(f"sni {name:20} {'pass' if allowed(name) else 'drop'}")
