"""Stand-in for OPA's Data API, for this lesson only; it is not OPA.

POST /v1/data/<path> with {"input": ...}. Answers {"result": value} when the
rule is defined and {} when it is not, which is how OPA answers. The policy
is the rules.py mirror of buckets.rego.
"""
import json
from http.server import BaseHTTPRequestHandler

import rules

POLICY = {"platform/buckets/allow": rules.allow,
          "platform/buckets/deny": rules.deny}


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        size = int(self.headers["Content-Length"])
        doc = json.loads(self.rfile.read(size))["input"]
        rule = POLICY.get(self.path.removeprefix("/v1/data/"))
        body = json.dumps({"result": rule(doc)} if rule else {}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass
