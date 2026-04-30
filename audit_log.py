from datetime import datetime, UTC
import uuid
from hashing import compute_hash
from storage import InMemoryStorage
from verify import verify_chain


class AuditLog:
    def __init__(self):
        self.storage = InMemoryStorage()

    def append_log(self, actor: str, action: str, data: dict = None) -> dict:
        last = self.storage.get_last()
        prev_hash = last["hash"] if last else None

        entry = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.now(UTC).isoformat(),
            "actor": actor,
            "action": action,
            "data": data or {},
            "prev_hash": prev_hash,
        }

        entry["hash"] = compute_hash(entry)

        self.storage.append(entry)

        return entry

    def verify(self) -> bool:
        return verify_chain(self.storage.get_all())