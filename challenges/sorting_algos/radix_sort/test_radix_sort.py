from .radix_sort import radix_sort
import random


def test_import():
    assert radix_sort


def test_sort_sorted_list_returns_same():
    assert radix_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_sort_even_list():
    assert radix_sort([3, 1, 4, 2]) == [1, 2, 3, 4]
    for i in range(100):
        rand_ints = [random.randint(1, 100) for i in range(4)]
        assert radix_sort(rand_ints) == sorted(rand_ints)

def test_sort_odd_list():
    assert radix_sort([3, 1, 2, 5, 4]) == [1, 2, 3, 4, 5]
    for i in range(100):
        rand_ints = [random.randint(1, 100) for i in range(5)]
        assert radix_sort(rand_ints) == sorted(rand_ints)

def test_sort_empty_list():
    assert radix_sort([]) == []


def test_sort_weird_digits():
    assert radix_sort([100, 10, 1]) == [1, 10, 100]
    assert radix_sort([15, 78, 100, 2, 9]) == [2, 9, 15, 78, 100]