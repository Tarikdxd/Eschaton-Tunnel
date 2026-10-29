# Eschaton-Tunnel

A small HTTP tunnel client written in Python with no third-party dependencies. It connects to a
relay server, registers a subdomain, and forwards incoming HTTP requests to a port on your
machine.

The client and the relay protocol are implemented in this repository. A public relay is not
guaranteed to be running: the default host, `relay.eschaton.io`, points at infrastructure that
may not serve this protocol. Point `--relay` at your own relay if the default does not respond.

## Requirements

Python 3.9 or newer. No packages to install.

## Usage

```bash
python main.py http 3000
python main.py http 8080 --subdomain demo
```

| Argument | Description |
| --- | --- |
| `port` | Local port to forward to |
| `--subdomain` | Request a stable subdomain instead of a random one |
| `--relay` | Relay host, default `relay.eschaton.io` |

## How it works

1. The client opens a connection to the relay and sends a registration message with the chosen
   subdomain and target port (`src/protocol.py`).
2. The relay sends each incoming HTTP request to the client as a JSON message.
3. `src/forwarder.py` replays the request against `127.0.0.1:<port>`.
4. The response travels back over the same connection and the relay returns it to the caller.

Requests are handled concurrently in `src/tunnel.py`.

## Tests

```bash
python -m unittest discover tests
```

## License

MIT. See [LICENSE](LICENSE).
