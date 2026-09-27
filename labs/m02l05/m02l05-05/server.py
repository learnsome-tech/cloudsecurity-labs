# Cloud Security & DevSecOps Engineering — lesson m02l05 — Zero-Trust Network Access & IdP Federation
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l05
# © LearnSome.tech
import json
from http.server import BaseHTTPRequestHandler
import broker

class Handler(BaseHTTPRequestHandler):
    def reply(self, status, text):
        self.send_response(status)
        self.end_headers()
        self.wfile.write(text.encode())

    def do_GET(self):  # every request to the app is decided here
        self.reply(*broker.decide(self.headers, now=1790000000))

    def do_PATCH(self):  # SCIM: PATCH /scim/v2/Users/{id}
        scim_id = self.path.removeprefix("/scim/v2/Users/")
        user = next(u for u in broker.USERS.values() if u["id"] == scim_id)
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        for op in body["Operations"]:
            if op["op"] == "replace" and op["path"] == "active":
                user["active"] = op["value"]
        self.reply(204, "")
