import os

from bpe_tokenizer import BPETokenizer
from download_text import getText

# Download the text only if we don't already have it
if not os.path.exists("the-verdict.txt"):
    getText()

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# Learn the merges from the text
tokenizer = BPETokenizer()
tokenizer.train(raw_text, vocab_size=300)

# Sanity check: encode then decode, the printed text should equal `text`
text = "It's the last he painted, you know."
ids = tokenizer.encode(text)
print(ids)
print(tokenizer.decode(ids))
