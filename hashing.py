import hashlib
import json

def compute_hash(entry: dict) -> str:
    entry_copy = dict(entry)
    entry_copy.pop("hash", None)

    payload = json.dumps(entry_copy, sort_keys=True).encode()
    return hashlib.sha256(payload).hexdigest()