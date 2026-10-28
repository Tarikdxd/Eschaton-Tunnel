import unittest
import asyncio
from src.protocol import TunnelMessage
from src.forwarder import LocalForwarder
from src.tunnel import TunnelSession

class TestEschatonTunnel(unittest.TestCase):

    def test_protocol_messages(self):
        reg = TunnelMessage.create_register(subdomain="my-api", target_port=8080)
        parsed = TunnelMessage.parse(reg)
        self.assertEqual(parsed["type"], TunnelMessage.TYPE_REGISTER)
        self.assertEqual(parsed["subdomain"], "my-api")
        self.assertEqual(parsed["target_port"], 8080)

        req = TunnelMessage.create_request("req-123", "POST", "/webhook", {"Authorization": "Bearer 123"}, "{}")
        p_req = TunnelMessage.parse(req)
        self.assertEqual(p_req["id"], "req-123")
        self.assertEqual(p_req["method"], "POST")

    def test_forwarder_bad_gateway(self):
        # Port 59999 is definitely not running
        fwd = LocalForwarder(target_port=59999)
        status, headers, body = fwd.forward("GET", "/", {})
        self.assertEqual(status, 502)
        self.assertIn("Bad Gateway", body)

    def test_tunnel_session_execution(self):
        async def run_test():
            session = TunnelSession("demo-sub", 59999)
            msg = {
                "id": "t-001",
                "method": "GET",
                "path": "/healthz",
                "headers": {}
            }
            res = await session.handle_incoming_request(msg)
            self.assertEqual(res["type"], TunnelMessage.TYPE_RESPONSE)
            self.assertEqual(res["id"], "t-001")
            self.assertEqual(res["status"], 502)

        asyncio.run(run_test())

if __name__ == "__main__":
    unittest.main()
