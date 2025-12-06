# Penetration Testing Toolkit (Python)

This modular toolkit is an **educational** internship project demonstrating basic penetration testing utilities.
**Legal & Ethical Notice:** Use this toolkit **only** on systems you own or have explicit written permission to test.

Included modules:
- run_toolkit.py         : CLI entry point to run modules
- toolkit/port_scanner.py: TCP connect port scanner (fast, no raw sockets)
- toolkit/http_bruteforce.py : HTTP Basic Auth brute-forcer (uses requests)
- toolkit/network_utils.py : shared utilities (threading, timing)
- docs/Documentation.md   : Brief documentation for submission
- requirements.txt
- examples/               : example usage and small wordlist

Penetration Testing Toolkit – Brief Documentation
1. Introduction

The Penetration Testing Toolkit is a modular, Python-based security toolkit designed for educational and authorized penetration testing.
It demonstrates core offensive security concepts such as:

Network reconnaissance

Port scanning

Password brute-forcing

Modular tool design

This toolkit was developed as part of a cybersecurity internship project and is intended to show understanding of penetration testing methodologies and Python automation.

2. Legal & Ethical Disclaimer

This toolkit is strictly for educational purposes and authorized penetration testing only.
You must NOT use these tools on any system unless you own it or have explicit written permission.

Unauthorized scanning or brute-forcing is illegal and violates cybersecurity laws.

3. Toolkit Overview

The toolkit includes two primary modules:

1. Port Scanner (TCP Connect Scan)

Scans a target host for open ports using TCP connect requests.

Uses multithreading for high performance.

No raw socket usage (works without root privileges).

Helps identify accessible network services for further testing.

2. HTTP Basic Authentication Brute-Forcer

Attempts to guess a user's password using a wordlist.

Uses HTTP Basic Auth and the requests library.

Supports multithreaded password attempts and adjustable delay.

Identifies weak or default credentials on protected endpoints.

4. File Structure
pt_toolkit/
├── run_toolkit.py                # Main CLI entry point
├── toolkit/
│   ├── port_scanner.py           # Port scanning module
│   ├── http_bruteforce.py        # Brute-force module
│   └── network_utils.py          # Shared utilities
├── docs/
│   └── Documentation.md          # Documentation file
├── examples/
│   ├── wordlist_small.txt        # Sample wordlist
│   └── README_EXAMPLES.md        # Example usage instructions
├── requirements.txt              # Python dependencies
└── README.md                     # Project overview

5. How to Install and Run
Step 1 — Install Requirements
pip install -r requirements.txt

Step 2 — Run the Toolkit

The toolkit provides two commands via run_toolkit.py.

A. Port Scan
python3 run_toolkit.py scan --host 192.168.1.10 --start 1 --end 1024 --workers 200


Parameters:

--host → target IP or hostname

--start / --end → port range

--workers → number of concurrent threads

--timeout → socket timeout (default 1s)

Output Example:

[*] Starting TCP connect scan…
[+] Port 22/tcp OPEN
[+] Port 80/tcp OPEN
[*] Scan completed in 3.21s.

B. HTTP Basic Auth Brute-Force
python3 run_toolkit.py bruteforce --url http://localhost/protected \
    --user admin \
    --wordlist examples/wordlist_small.txt \
    --workers 10


Behavior:

Loads every password in the wordlist

Attempts login using HTTP Basic Auth

Reports a SUCCESS when a valid credential is found

6. How the Modules Work
Port Scanner

Uses Python’s socket library to attempt TCP connections.

If a connection succeeds → port is OPEN.

Multi-threading improves speed.

Brute-Forcer

Sends HTTP GET requests with Basic Auth header.

If the server returns 200 OK, the password is considered valid.

Multi-threaded execution allows high-speed testing.

7. Limitations

This toolkit is intentionally simplified for internship-level learning:

No UDP scanning

No service version detection

Brute-force module only supports HTTP Basic Auth

No credential lockout detection

Not suitable for stealthy or large-scale penetration tests

8. Possible Enhancements

To expand the project, you can add:

UDP port scanning (requires raw sockets)

Banner grabbing & service fingerprinting

Logging & reporting output (CSV/HTML)

SSH/FTP brute-force modules

Retry/backoff mechanisms

Plugin-based architecture

These improvements can significantly increase the professionalism of the toolkit.

9. Conclusion

The Penetration Testing Toolkit demonstrates foundational penetration testing techniques using Python.
It provides a modular, extensible structure and serves as a strong starting point for building more advanced security tools.

This toolkit fulfills the internship task requirements by delivering:

✔ A Python-based modular security toolkit
✔ Working port scanner
✔ Working brute-forcer
✔ Clear documentation
✔ Ethical and safe usage guidelines
