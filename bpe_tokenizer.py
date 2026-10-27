from collections import Counter


class BPETokenizer:
    def __init__(self):
        self.merges = {}  # (id, id) -> new id
        self.vocab = {i: bytes([i]) for i in range(256)}  # id -> bytes

    def train(self, text, vocab_size):
        # 1. text -> list of utf-8 byte ints
        ids = list(text.encode("utf-8"))

        # 2. repeat: find most common pair, merge it into a new id, record it
        for new_id in range(256, vocab_size):
            counts = Counter(zip(ids, ids[1:]))
            if not counts:
                break  # fewer than 2 ids left, nothing to merge
            pair = counts.most_common(1)[0][0]

            ids = self.merge(ids, pair, new_id)
            self.merges[pair] = new_id
            self.vocab[new_id] = self.vocab[pair[0]] + self.vocab[pair[1]]

    def merge(self, ids, pair, new_id):
        # replace every adjacent `pair` in ids with new_id
        output = []
        i = 0
        while i < len(ids):
            if i < len(ids) - 1 and (ids[i], ids[i+1]) == pair:
                output.append(new_id)
                i += 2
            else:
                output.append(ids[i])
                i += 1

        return output

    def encode(self, text):
        # text -> bytes -> apply merges (earliest learned first)
        ids = list(text.encode("utf-8"))
        while len(ids) >= 2:
            pairs = set(zip(ids, ids[1:]))
            # pick the pair that was learned earliest (lowest merged id)
            pair = min(pairs, key=lambda p: self.merges.get(p, float("inf")))
            if pair not in self.merges:
                break  # none of the remaining pairs can be merged
            ids = self.merge(ids, pair, self.merges[pair])
        return ids

    def decode(self, ids):
        # ids -> bytes via vocab -> string
        data = b"".join(self.vocab[i] for i in ids)
        return data.decode("utf-8", errors="replace")
