from collections import defaultdict

class MemoryService:
    def __init__(self):
        self.sessions = defaultdict(list)
        self.memory_bank = defaultdict(dict)

    def write(self, user_id, parsed, verdict):
        self.sessions[user_id].append({"parsed": parsed, "verdict": verdict})
        # keep last 20 interactions
        self.sessions[user_id] = self.sessions[user_id][-20:]
        stats = self.memory_bank[user_id].get('stats', {'claims': 0})
        stats['claims'] = stats.get('claims', 0) + 1
        self.memory_bank[user_id]['stats'] = stats

    def read_session(self, user_id):
        return self.sessions[user_id]

    def read_longterm(self, user_id):
        return self.memory_bank[user_id]
