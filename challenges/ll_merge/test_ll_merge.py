from .linked_list import LinkedList
from .ll_merge import ll_merge
import pytest


def test_ll_merge_equal_length_lls():
    """Test return of two equal length lists."""
    ll2 = LinkedList([1, 3])
    ll1 = LinkedList([2, 4])
    expected = '[4, 3, 2, 1]'
    assert str(ll_merge(ll1, ll2)) == expected


def test_ll_merge_equal_length_lls_2():
    """Test return of two longer lists."""
    ll2 = LinkedList([1, 3, 5, 7])
    ll1 = LinkedList([2, 4, 6, 8])
    expected = '[8, 7, 6, 5, 4, 3, 2, 1]'
    assert str(ll_merge(ll1, ll2)) == expected


def test_ll_merge_different_length_lls():
    """Test return of two unequal length lists."""
    ll2 = LinkedList([4, 2])
    ll1 = LinkedList([5, 3, 1])
    expected = '[1, 2, 3, 4, 5]'
    assert str(ll_merge(ll1, ll2)) == expected


def test_ll_merge_empties():
    """Test return of two empty lists."""
    ll1 = LinkedList([])
    ll2 = LinkedList([])
    expected = '[]'
    assert str(ll_merge(ll1, ll2)) == expected


def test_ll_merge_one_empty():
    """Test return with first list empty."""
    ll1 = LinkedList([])
    ll2 = LinkedList([2, 3, 5, 7, 11, 13])
    expected = '[13, 11, 7, 5, 3, 2]'
    assert str(ll_merge(ll1, ll2)) == expected


def test_ll_merge_second_empty():
    """Test return with second list empty."""
    ll1 = LinkedList([])
    ll2 = LinkedList([2, 3, 5, 7, 11, 13])
    expected = '[13, 11, 7, 5, 3, 2]'
    assert str(ll_merge(ll2, ll1)) == expected
