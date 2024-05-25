import hashlib
import bc_log as log

def hashing(string: str) -> str:
    return hashlib.sha256(string.encode("utf-8")).hexdigest()

def blockchane(string: str):
    if len(log.logs) == 0:
        hash = hashing(f"{string}")
        log.logs.append(hash)
    else:
        last = log.logs[len(log.logs)-1]
        hash = hashing(f"{last} {string}")
        log.logs.append(hash)