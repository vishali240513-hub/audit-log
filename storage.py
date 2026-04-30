class InMemoryStorage:
    def __init__(self):
        self.logs = []

    def append(self, entry: dict):
        self.logs.append(entry)

    def get_all(self):
        return self.logs

    def get_last(self):
        return self.logs[-1] if self.logs else None