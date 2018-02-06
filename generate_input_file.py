#!/usr/bin/env python3

import itertools
import random
import string

delimiters = (' ', '.', ',', '!', '?', ':', ';', '"', "'", '\n', '-', '_')


def get_delimiter() -> str:
    return random.choice(delimiters)


def get_symbol() -> str:
    return random.choice(string.ascii_letters)


def get_word() -> str:
    return ''.join(get_symbol() for _ in range(random.randint(3, 10)))


if __name__ == '__main__':
    words = itertools.cycle([get_word() for _ in range(10)])
    with open('input_file.txt', mode='w') as f:
        for _ in range(random.randint(20, 50)):
            f.write(f'{next(words)}{get_delimiter()}')
