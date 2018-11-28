from .array_binary_search import binary_search


def test_test_suite_works():
    """Test for basic functionality in pytest."""


def test_binary_search_exists():
    """Test binary_search function successfully imported."""
    assert binary_search


def test_binary_search():
    """3 elements, key in middle."""
    assert binary_search([1, 2, 3], 2) == 1


def test_binary_search_2():
    """3 elements, key in left half."""
    assert binary_search([1, 2, 3, 4], 2) == 1


def test_binary_search_3():
    """4 elements, key at 0."""
    assert binary_search([1, 2, 3, 4], 1) == 0


def test_binary_search_4():
    """3 elements, key not in list."""
    assert binary_search([1, 2, 3], 4) == -1


# def test_binary_search_4():
#     """ 10 elements, key in right half.
#     """
#     test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     key = 7
#     actual = 6
#     assert binary_search(test_list, key) == actual
