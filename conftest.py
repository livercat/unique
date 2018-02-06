import os
from collections import Counter

import pytest


@pytest.fixture
def input_file() -> str:
    return os.path.join(os.path.dirname(__file__), 'tests', 'test_input_file.txt')


@pytest.fixture
def predefined_count() -> Counter:
    return Counter(
        {'this': 2,
         'is': 2,
         'a': 2,
         'test': 2,
         'file': 2,
         'with': 1,
         'some': 1,
         'different': 1,
         'word': 1,
         'boundaries': 1,
         'and': 4,
         'AND': 2,
         'And': 1}
    )
