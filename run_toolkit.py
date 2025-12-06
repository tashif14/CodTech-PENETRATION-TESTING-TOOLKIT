#!/usr/bin/env python3
"""Entry point for the Penetration Testing Toolkit.
Usage examples:
  python3 run_toolkit.py scan --host 192.168.1.10 --start 20 --end 1024 --workers 100
  python3 run_toolkit.py bruteforce --url http://localhost:8080/protected --user admin --wordlist examples/wordlist_small.txt --workers 10
"""
import argparse
from toolkit.port_scanner import tcp_connect_scan
from toolkit.http_bruteforce import http_basic_bruteforce

def main():
    parser = argparse.ArgumentParser(description='Penetration Testing Toolkit (educational)')
    sub = parser.add_subparsers(dest='cmd', required=True)

    p_scan = sub.add_parser('scan', help='TCP connect port scanner')
    p_scan.add_argument('--host', required=True, help='Target host (IP or hostname)')
    p_scan.add_argument('--start', type=int, default=1, help='Start port (default 1)')
    p_scan.add_argument('--end', type=int, default=1024, help='End port (default 1024)')
    p_scan.add_argument('--timeout', type=float, default=1.0, help='Socket timeout (seconds)')
    p_scan.add_argument('--workers', type=int, default=100, help='Concurrent worker threads')

    p_brute = sub.add_parser('bruteforce', help='HTTP Basic Auth brute-forcer')
    p_brute.add_argument('--url', required=True, help='Target URL protected by Basic Auth (include scheme)')
    p_brute.add_argument('--user', required=True, help='Username to try')
    p_brute.add_argument('--wordlist', required=True, help='Path to password wordlist (one per line)')
    p_brute.add_argument('--workers', type=int, default=10, help='Concurrent workers')
    p_brute.add_argument('--delay', type=float, default=0.1, help='Delay between requests per worker (s)')

    args = parser.parse_args()

    if args.cmd == 'scan':
        tcp_connect_scan(args.host, args.start, args.end, timeout=args.timeout, workers=args.workers)
    elif args.cmd == 'bruteforce':
        http_basic_bruteforce(args.url, args.user, args.wordlist, workers=args.workers, delay=args.delay)

if __name__ == '__main__':
    main()
