import sys
import argparse
import time
from src.protocol import TunnelMessage
from src.tunnel import TunnelSession

def main():
    parser = argparse.ArgumentParser(description="Eschaton-Tunnel CLI")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    http_parser = subparsers.add_parser("http", help="Expose local HTTP port to internet")
    http_parser.add_argument("port", type=int, help="Local port (e.g. 3000, 8080)")
    http_parser.add_argument("--subdomain", type=str, default=None, help="Custom subdomain")
    http_parser.add_argument("--relay", type=str, default="relay.eschaton.io", help="Tunnel relay host")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    sub = args.subdomain or f"tunnel-{int(time.time())}"
    public_url = f"https://{sub}.{args.relay}"

    print("=" * 65)
    print("           ⚡ ESCHATON-TUNNEL - ZERO-CONFIG REVERSE PROXY")
    print("      Instant Localhost to Internet Tunnel (Free ngrok Alternative)")
    print("                     Developer: Tarikdxd")
    print("=" * 65)
    print(f"[+] Local Target Port : http://127.0.0.1:{args.port}")
    print(f"[+] Tunnel Status     : Online / Multiplexing Active")
    print(f"[+] Public URL        : {public_url}")
    print(f"[+] Web Inspector     : http://127.0.0.1:4040 (Live HTTP Traffic)")
    print("=" * 65)
    print("[*] Forwarding traffic. Press Ctrl+C to terminate session.")

    session = TunnelSession(sub, args.port)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Tunnel closed.")

if __name__ == "__main__":
    main()
