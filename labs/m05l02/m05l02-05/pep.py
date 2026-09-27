# Cloud Security & DevSecOps Engineering — lesson m05l02 — Policy-as-Code Architecture: OPA & Rego Syntax
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m05l02
# © LearnSome.tech
import json, threading, urllib.request
from http.server import HTTPServer
from opa_standin import Handler  # same request and response shape as OPA

server = HTTPServer(("127.0.0.1", 0), Handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{server.server_port}/v1/data/"

def query(path, doc):
    body = json.dumps({"input": doc}).encode()
    req = urllib.request.Request(base + path, body, method="POST")
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)

ben = {"user": {"name": "ben", "team": "payments"}, "action": "read",
       "bucket": {"name": "hr-records", "owner": "people"}}
for path in ["platform/buckets/allow", "platform/bucket/allow"]:
    answer = query(path, ben)
    naive = answer.get("result") is not False
    closed = answer.get("result") is True
    print(f"{path}: {json.dumps(answer)} naive={naive} closed={closed}")
server.shutdown()
