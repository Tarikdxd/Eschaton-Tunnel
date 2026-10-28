import json
import uuid
from typing import Dict, Any, Optional

class TunnelMessage:
    """Wire protocol messaging for Eschaton-Tunnel multiplexing."""
    
    TYPE_REGISTER = "REGISTER"
    TYPE_REGISTERED = "REGISTERED"
    TYPE_REQUEST = "REQUEST"
    TYPE_RESPONSE = "RESPONSE"
    TYPE_PING = "PING"
    TYPE_PONG = "PONG"
    TYPE_ERROR = "ERROR"

    @staticmethod
    def create_register(subdomain: Optional[str] = None, target_port: int = 3000) -> str:
        return json.dumps({
            "type": TunnelMessage.TYPE_REGISTER,
            "subdomain": subdomain or f"tun-{uuid.uuid4().hex[:8]}",
            "target_port": target_port
        })

    @staticmethod
    def create_request(req_id: str, method: str, path: str, headers: Dict[str, str], body: str = "") -> str:
        return json.dumps({
            "type": TunnelMessage.TYPE_REQUEST,
            "id": req_id,
            "method": method,
            "path": path,
            "headers": headers,
            "body": body
        })

    @staticmethod
    def create_response(req_id: str, status: int, headers: Dict[str, str], body: str) -> str:
        return json.dumps({
            "type": TunnelMessage.TYPE_RESPONSE,
            "id": req_id,
            "status": status,
            "headers": headers,
            "body": body
        })

    @staticmethod
    def parse(raw_str: str) -> Dict[str, Any]:
        return json.loads(raw_str)
