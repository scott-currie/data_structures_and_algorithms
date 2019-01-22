import pytest
import random
from .selection import selection_sort


def test_import():
    assert selection_sort


def test_selection_sort_ints():
    assert selection_sort([3, 1, 2]) == [1, 2, 3]
    rand_ints = [random.randint(1, 100) for i in range(100)]
    assert selection_sort(rand_ints) == sorted(rand_ints)


def test_selection_sort_strings():
    assert selection_sort(['one', 'two', 'three']) == ['one', 'three', 'two']


def test_selection_sort_empty():
    assert selection_sort([]) == []


def test_selection_sort_non_list_exception():
    with pytest.raises(TypeError):
        selection_sort({})
