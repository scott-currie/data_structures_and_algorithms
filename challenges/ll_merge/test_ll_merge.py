from .linked_list import LinkedList
from .ll_merge import ll_merge


def test_ll_merge_equal_length_lls():
    ll2 = LinkedList([10, 8, 6, 4, 2])
    ll1 = LinkedList([9, 7, 5, 3, 1])
    expected = '[1, 2, 3, 4, 5, 6]'
    assert str(ll_merge(ll1, ll2)) == expected


def test_ll_merge_different_length_lls():
    ll2 = LinkedList([4, 2])
    ll1 = LinkedList([5, 3, 1])
    expected = '[1, 2, 3, 4, 5]'
    assert str(ll_merge(ll1, ll2)) == expected
