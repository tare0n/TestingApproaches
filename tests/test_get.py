from get import get


def test_get():
    assert get([1, 2, 3], 1, "a") == 2
    assert get([4, 5, 6], 7, "val") == "val"


def test_get_incorrect_values():
    assert get("    ", -1) is None
    assert get('a', 2) is None


