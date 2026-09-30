"""Starts the broker on 127.0.0.1 and makes requests to it."""
import threading
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer

from server import Handler

Handler.log_message = lambda *args: None  # keep request logs out of the output
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def start():
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return f"http://127.0.0.1:{server.server_port}"


def send(request):
    try:
        with opener.open(request) as resp:
            return resp.status, resp.read().decode()
    except urllib.error.HTTPError as err:
        return err.code, err.read().decode()


def get(base, token, device):
    return send(urllib.request.Request(f"{base}/payroll", headers={
        "Authorization": f"Bearer {token}", "X-Device-Id": device}))
