"""Shared utilities for the toolkit"""
import socket, time
from concurrent.futures import ThreadPoolExecutor, as_completed

def chunk_ports(start, end, workers):
    """Yield lists of ports to scan per worker if needed (not used directly)"""
    ports = list(range(start, end+1))
    k = max(1, len(ports)//workers)
    for i in range(0, len(ports), k):
        yield ports[i:i+k]
