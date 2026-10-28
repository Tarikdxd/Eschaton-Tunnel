<div align="center">

# ⚡ Eschaton-Tunnel

**Instant, Zero-Config Localhost to Internet Reverse Proxy & Public Tunneling CLI**

*A free, open-source, and lightweight alternative to ngrok and Cloudflare Tunnels.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red.svg)](https://github.com/Tarikdxd/Eschaton-Tunnel)
[![No Cloud Sign-up](https://img.shields.io/badge/Account-Not%20Required-brightgreen.svg)]()

---

</div>

## ✨ Why Eschaton-Tunnel?

Most tunneling tools (like ngrok) have added mandatory accounts, strict session timeouts, and bandwidth throttles. **Eschaton-Tunnel** provides a direct, developer-first tunnel client and relay server designed for local webhook testing, mobile debugging, and showcasing projects to clients.

- 🚀 **One-Command Setup:** Expose your local web server in seconds (`eschaton-tunnel http 3000`).
- 🔐 **End-to-End HTTPS:** Automatic TLS encryption for all incoming web requests.
- 🩺 **Live Webhook & Traffic Inspector:** Inspect incoming GET/POST requests, HTTP headers, payloads, and response times in real time.
- 🌐 **Custom Subdomain Support:** Request persistent subdomains (`--subdomain my-api`).
- 🪶 **Zero Heavy Dependencies:** Minimal resource footprint.

---

## 🚀 Quick Start

### 1. Installation & Usage
```bash
git clone https://github.com/Tarikdxd/Eschaton-Tunnel.git
cd Eschaton-Tunnel
python main.py http 3000
```

### 2. Custom Subdomain
```bash
python main.py http 8080 --subdomain test-webhook
```

Output:
```text
=================================================================
           ⚡ ESCHATON-TUNNEL - ZERO-CONFIG REVERSE PROXY
      Instant Localhost to Internet Tunnel (Free ngrok Alternative)
                     Developer: Tarikdxd
=================================================================
[+] Local Target Port : http://127.0.0.1:8080
[+] Tunnel Status     : Online / Multiplexing Active
[+] Public URL        : https://test-webhook.relay.eschaton.io
[+] Web Inspector     : http://127.0.0.1:4040 (Live HTTP Traffic)
=================================================================
```

---

## 🧪 Tests

```bash
python -m unittest discover tests
```

---

## 📄 License

Distributed under the [MIT License](LICENSE).
