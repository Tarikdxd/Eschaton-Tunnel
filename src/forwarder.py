import urllib.request
import urllib.error
from typing import Dict, Tuple

class LocalForwarder:
    """Forwards incoming tunneled HTTP requests to the target localhost port."""

    def __init__(self, target_host: str = "127.0.0.1", target_port: int = 3000):
        self.target_host = target_host
        self.target_port = target_port

    def forward(self, method: str, path: str, headers: Dict[str, str], body: str = "") -> Tuple[int, Dict[str, str], str]:
        url = f"http://{self.target_host}:{self.target_port}{path}"
        data = body.encode("utf-8") if body else None
        
        # Filter forbidden headers for urllib
        clean_headers = {k: v for k, v in headers.items() if k.lower() not in ("host", "content-length")}

        req = urllib.request.Request(url, data=data, headers=clean_headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=10.0) as resp:
                resp_body = resp.read().decode("utf-8", errors="replace")
                resp_headers = dict(resp.headers)
                return resp.status, resp_headers, resp_body
        except urllib.error.HTTPError as e:
            return e.code, dict(e.headers), e.read().decode("utf-8", errors="replace")
        except urllib.error.URLError as e:
            err_html = f"<html><body><h2>502 Bad Gateway</h2><p>Eschaton-Tunnel failed to connect to local service on port {self.target_port}: {e.reason}</p></body></html>"
            return 502, {"Content-Type": "text/html"}, err_html
