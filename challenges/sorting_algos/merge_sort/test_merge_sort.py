from .merge_sort import merge_sort
import random


def test_import():
    assert merge_sort


def test_sort_even_list():
    assert merge_sort([3, 1, 4, 2]) == [1, 2, 3, 4]
    for i in range(100):
        rand_ints = [random.randint(1, 100) for i in range(4)]
        assert merge_sort(rand_ints) == sorted(rand_ints)


def test_sort_odd_list():
    assert merge_sort([3, 1, 2, 5, 4]) == [1, 2, 3, 4, 5]
    for i in range(100):
        rand_ints = [random.randint(1, 100) for i in range(5)]
        assert merge_sort(rand_ints) == sorted(rand_ints)


def test_sort_empty_list():
    assert merge_sort([]) == []