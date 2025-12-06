"""TCP connect port scanner (no raw sockets) - educational use only"""
import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def _scan_port(host, port, timeout=1.0):
    """Attempt TCP connect on host:port. Return True if open."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        s.close()
        return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False
    except Exception:
        return False

def tcp_connect_scan(host, start=1, end=1024, timeout=1.0, workers=100):
    """Perform a concurrent TCP connect scan over port range."""
    ports = list(range(start, end+1))
    print(f"[*] Starting TCP connect scan on {host} ports {start}-{end} with {workers} workers") 
    open_ports = []
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(_scan_port, host, p, timeout): p for p in ports}
        for fut in as_completed(futures):
            p = futures[fut]
            try:
                if fut.result():
                    print(f"[+] Port {p}/tcp OPEN")
                    open_ports.append(p)
            except Exception as e:
                pass
    duration = time.time() - start_time
    print(f"[*] Scan completed in {duration:.2f}s. Open ports: {open_ports}")
    return open_ports
