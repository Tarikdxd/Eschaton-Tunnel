import asyncio
from typing import Dict, Tuple
from .protocol import TunnelMessage
from .forwarder import LocalForwarder

class TunnelSession:
    """Manages active tunnel multiplexing, request tracking, and response relaying."""

    def __init__(self, subdomain: str, local_port: int):
        self.subdomain = subdomain
        self.local_port = local_port
        self.forwarder = LocalForwarder(target_port=local_port)
        self.active_requests: Dict[str, asyncio.Future] = {}

    async def handle_incoming_request(self, msg: dict) -> dict:
        req_id = msg.get("id")
        method = msg.get("method", "GET")
        path = msg.get("path", "/")
        headers = msg.get("headers", {})
        body = msg.get("body", "")

        loop = asyncio.get_running_loop()
        status, resp_headers, resp_body = await loop.run_in_executor(
            None, self.forwarder.forward, method, path, headers, body
        )

        return {
            "type": TunnelMessage.TYPE_RESPONSE,
            "id": req_id,
            "status": status,
            "headers": resp_headers,
            "body": resp_body
        }
