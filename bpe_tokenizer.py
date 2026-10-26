from collections import Counter


class BPETokenizer:
    def __init__(self):
        self.merges = {}  # (id, id) -> new id
        self.vocab = {i: bytes([i]) for i in range(256)}  # id -> bytes

    def train(self, text, vocab_size):
        # 1. text -> list of utf-8 byte ints
        # 2. repeat: find most common pair, merge it into a new id, record it
        pass

    def merge(self, ids, pair, new_id):
        # replace every adjacent `pair` in ids with new_id
        pass

    def encode(self, text):
        # text -> bytes -> apply merges (earliest learned first)
        pass

    def decode(self, ids):
        # ids -> bytes via vocab -> string
        pass
