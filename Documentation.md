# Penetration Testing Toolkit - Documentation

## Legal & Ethical Notice
This toolkit is for educational and authorized penetration testing only.
Do not use this toolkit on systems you do not own or do not have explicit written permission to test.

## Overview
The toolkit contains two primary modules:
1. **Port Scanner** - TCP connect scanner using concurrent threads.
2. **HTTP Basic Auth Brute-Forcer** - Attempts passwords from a wordlist using HTTP Basic Auth.

## How to run
Install dependencies:
    pip install -r requirements.txt

Examples:
    python3 run_toolkit.py scan --host 192.168.1.10 --start 20 --end 1024 --workers 200
    python3 run_toolkit.py bruteforce --url http://localhost:8080/protected --user admin --wordlist examples/wordlist_small.txt --workers 10

## Implementation notes
- Port scanner uses TCP connect (no raw sockets), so it works without root privileges.
- Brute-forcer uses requests and treats HTTP 200 as success; modify per target behavior.
- Both modules are intentionally simple and safe-by-default (rate-limiting possible via delay args).

## Enhancements (suggestions)
- Add UDP scanning (requires raw sockets and root).
- Add service detection (banner grabbing).
- Add retry/backoff (tenacity) and logging to files.
- Integrate SSH/FTP brute-forcers (paramiko, ftplib).
- Create a CLI with subcommands and configuration profiles.
