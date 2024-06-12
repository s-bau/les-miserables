import pandas as pd
import re
import requests

tout = {"tome_1": "https://gutenberg.org/cache/epub/17489/pg17489.txt",
        "tome_2": "https://gutenberg.org/cache/epub/17493/pg17493.txt",
        "tome_3": "https://gutenberg.org/cache/epub/17494/pg17494.txt",
        "tome_4": "https://gutenberg.org/cache/epub/17518/pg17518.txt",
        "tome_5": "https://gutenberg.org/cache/epub/17519/pg17519.txt"}

miserables = dict()

for k, v in tout.items():
    url = v
    response = requests.get(url)

    if response.status_code == 200:
        miserables[k] = response.text
    else:
        print(f"Failed to retrieve file. Status code: {response.status_code}")

miserables_full = ""

# taking out metatext that's not part of Les Misérables
for k, v in miserables.items():
    tome = v
    pattern = r'(?:.*?Livre premier--.*?){2}(.*)\*\*\* END OF THE PROJECT GUTENBERG EBOOK LES MISÉRABLES'
    tome = re.search(pattern, tome, re.DOTALL).group(1).strip()
    miserables_full += tome

    # # test prints
    # print(f"Start: {tome[:50]}")
    # print(f"End: {tome[-50:]}")
    # print()