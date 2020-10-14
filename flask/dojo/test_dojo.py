import pytest

# content of test_sample.py
def inc(x):
    return x + 0.5 + 0.5

@pytest.mark.parametrize("num, result", [
    (6, 7),
    (3, 4),
    (-3, -2),
    (0, 1),
    (5555555555, 5555555556)
])
def test_inc(num, result):
    # implement here
    assert inc(num) == result
