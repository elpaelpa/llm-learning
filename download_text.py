import os
import urllib.request
import re

# Get Raw text

def getText():
    url = ("https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt")
    file_path = "the-verdict.txt"
    urllib.request.urlretrieve(url, file_path)

if __name__ == "__main__":
    if not os.path.exists("the-verdict.txt"):
        getText()

    with open("the-verdict.txt","r",encoding="utf-8") as f:
        raw_text = f.read()

    print("Total number of character:" , len(raw_text))

    short_text= raw_text[:99]
    print(short_text)

    result = re.split(r'(\s)',short_text)
    print(result)

