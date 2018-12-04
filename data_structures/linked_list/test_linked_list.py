from linked_list import LinkedList
import pytest


@pytest.fixture
def empty_ll():
    return LinkedList()


@pytest.fixture
def small_ll():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll


@pytest.fixture
def random_ll():
    from random import randint
    ll = LinkedList()
    for num in range(100):
        ll.insert(randint(0, 100))
    return ll


def test_ll_module_exists():
    assert LinkedList


def test_ll_instance_has_none_value_head(empty_ll):
    assert empty_ll.head is None


def test_ll_str_method(empty_ll):
    assert str(empty_ll) == '[]'


def test_ll_str_method():
    """Test the rewritten str method behaves like the one for lists."""
    ll = LinkedList([1, 2, 3])
    expected = '[3, 2, 1]'
    assert str(ll) == expected


def test_size_of_empty_ll(empty_ll):
    assert len(empty_ll) == 0


def test_small_fixture_has_size_of_4(small_ll):
    assert len(small_ll) == 4


def test_insert_new_node_into_empty_list(empty_ll):
    assert empty_ll.head is None
    empty_ll.insert(1)
    assert empty_ll.head.val == 1


def test_random_ll(random_ll):
    assert len(random_ll) == 100


def test_iterable_as_argument():
    ll = LinkedList([1, 2, 3, 4])
    assert ll.head.val == 4
    assert len(ll) == 4


def test_ll_includes_finds_target():
    """Test LinkedList instance method includes returns true if value to find is in the list."""
    ll = LinkedList([1, 2, 3, 4])
    assert ll.includes(4)


def test_ll_includes_returns_false():
    """Test LinkedList instance method includes returns false if value to find is not in the list."""
    ll = LinkedList([1, 2, 3, 4])
    assert not ll.includes(9)


def test_append_includes_val_non_empty_list():
    """Add a new value to LL with insert method, then test the LL includes the new value."""
    ll = LinkedList([1, 2, 3])
    ll.insert(4)
    assert ll.includes(4)


def test_append_includes_val_empty_list(empty_ll):
    """Add a new value to empty LL with insert method, then test the LL includes the new value."""
    empty_ll.append(4)
    assert empty_ll.includes(4)


def test_insert_before_non_empty_list():
    """Test the str representation of non-empty LL matches expected after insert_before is called on it."""
    ll = LinkedList([1, 2, 3])
    ll.insert_before(3, 4)
    assert ll.includes(4)
    assert str(ll) == '[4, 3, 2, 1]'


def test_insert_after_non_empty_list():
    """Test the str representation of empty LL matches expected after insert_before is called on it."""
    ll = LinkedList([1, 2, 3])
    ll.insert_after(2, 4)
    assert ll.includes(4)
    assert str(ll) == '[3, 2, 4, 1]'


def test_kth_from_end_k_too_big_raises_exception(small_ll):
    """Test kth_from_end with small_ll and k > length of list raises IndexError."""
    with pytest.raises(IndexError):
        small_ll.kth_from_end(5)


def test_kth_from_end_k_lt_length():
    """Test kth_from_end with small_ll and k less than len(small_ll)"""
    ll = LinkedList([2, 8, 3, 1])
    expected = 3
    assert ll.kth_from_end(2) == expected


def test_kth_from_end_k_is_0(small_ll):
    expected = 1
    assert small_ll.kth_from_end(0) == expected
