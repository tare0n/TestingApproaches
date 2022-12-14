from index_of import index_of
numbers = [2, 7, 3, 2, 4]


def test_index_of():
    assert index_of(numbers, 2) == 0


def test_index_of_out_of_range():
    assert index_of(numbers, 10) == -1


def test_index_of_empty_coll():
    assert index_of("", 2) == -1


def test_index_of_negative_index():
    assert index_of(numbers, 2, -2) == 3
    assert index_of(numbers, 2, -10) == 0
