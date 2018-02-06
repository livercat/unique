import re
from collections import Counter, defaultdict
from typing import Dict

# re maintains internal cache of recent compiled expression, but we're compiling and storing it for clarity anyway
word_re = re.compile('[a-zA-Z]+')


# will eat all the memory if the file is a huge single line
def process(file: str) -> Dict[str, int]:
    result = Counter()
    with open(file) as f:
        for line in f:
            for match in word_re.findall(line):
                result[match] += 1
    return result


def render(d: Dict[str, int]) -> str:
    buckets = defaultdict(set)
    for word, count in d.items():
        buckets[count].add(word)
    result = ''
    for count, words in sorted(buckets.items(), reverse=True):  # sort by count
        for word in sorted(words, key=lambda w: (w.lower(), len(w))):  # sort by alphabet
            result += f'{word}: {count}\n'
    return result.strip()
