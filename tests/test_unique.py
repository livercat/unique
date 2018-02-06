from src import processing


def test_process(input_file, predefined_count):
    assert processing.process(input_file) == predefined_count


def test_render(predefined_count):
    expected = """and: 4
a: 2
AND: 2
file: 2
is: 2
test: 2
this: 2
And: 1
boundaries: 1
different: 1
some: 1
with: 1
word: 1"""
    assert processing.render(predefined_count) == expected
