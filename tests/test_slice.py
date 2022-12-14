from slice import my_slice
numbers = [1, 2, 3, 4, 5, 6]


def test_slice():
    assert my_slice(numbers, 1, 4) == [2, 3, 4]


def test_slice_if_empty():
    assert my_slice([], 1, 4) == []


def test_slice_with_negative_index():
    assert my_slice(numbers, -10, 4) == [1, 2, 3, 4]
    assert my_slice(numbers, -4, 4) == [3, 4]
