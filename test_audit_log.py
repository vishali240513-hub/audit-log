from audit_log import AuditLog


def test_first_log_has_no_prev_hash():
    log = AuditLog()
    entry = log.append_log("user", "TEST")

    assert entry["prev_hash"] is None
    assert entry["hash"] is not None


def test_logs_are_linked():
    log = AuditLog()
    log1 = log.append_log("user", "A")
    log2 = log.append_log("user", "B")

    assert log2["prev_hash"] == log1["hash"]


def test_verify_valid_chain():
    log = AuditLog()
    log.append_log("u", "A")
    log.append_log("u", "B")

    assert log.verify() is True   

def test_tampering_detected():
    log = AuditLog()
    log.append_log("u", "A")
    log.append_log("u", "B")

    logs = log.storage.get_all()   
    logs[1]["action"] = "HACKED"

    assert log.verify() is False   


def test_reordering_breaks_chain():
    log = AuditLog()
    log.append_log("u", "A")
    log.append_log("u", "B")

    logs = log.storage.get_all()  
    logs.reverse()

    assert log.verify() is False   