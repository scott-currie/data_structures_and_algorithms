from .quicksort import quicksort
import random


def test_import():
    assert quicksort


def test_sort_even_list():
    assert quicksort([3, 1, 4, 2]) == [1, 2, 3, 4]
    for i in range(100):
        rand_ints = [random.randint(1, 100) for i in range(4)]
        assert quicksort(rand_ints) == sorted(rand_ints)


def test_sort_odd_list():
    assert quicksort([3, 1, 2, 5, 4]) == [1, 2, 3, 4, 5]
    for i in range(100):
        rand_ints = [random.randint(1, 100) for i in range(5)]
        assert quicksort(rand_ints) == sorted(rand_ints)


def test_sort_empty_list():
    assert quicksort([]) == []