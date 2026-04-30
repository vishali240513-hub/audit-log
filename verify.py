from hashing import compute_hash
def verify_chain(logs: list) -> bool:
    for i in range(len(logs)):
        entry = logs[i]

        if entry["hash"] != compute_hash(entry):
            return False

        if i > 0 and entry["prev_hash"] != logs[i - 1]["hash"]:
            return False

        if i == 0 and entry["prev_hash"] is not None:
            return False

    return True