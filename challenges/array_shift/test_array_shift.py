from .array_shift import insertArrayShift
import pytest

def test_pytest_works():
    """Test to see if the test suite is running successfully."""
    assert True is True

def test_insert_array_shift_exists():
    """Test to insure the inserArrayShift function exists"""
    assert insertArrayShift

def test_insert_array_shift_even_items():
    """"Test the function against an array with an even number of items. Success returns the array with 0 inserted at idx=2.
    """
    to_insert = 0
    actual = [1, 2, 3, 4]
    expected = [1, 2, 0, 3, 4]
    assert insertArrayShift(actual, to_insert) == expected

def test_insert_array_shift_odd_items():
    """"Test the function against an array with an odd number of items. Success returns the array with 0 inserted at idx=3.
    """
    to_insert = 0
    actual = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 0, 4, 5]
    assert insertArrayShift(actual, to_insert) == expected

def test_insert_array_shift_empty_list():
    """"Test the function against an empty array. Success returns the array with 0 as the only element.
    """
    to_insert = 0
    actual = []
    expected = [0]
    assert insertArrayShift(actual, to_insert) == expected

def test_insert_array_shift_strings():
    to_insert = 'q'
    actual = ['a', 'e', 'i', 'o', 'u']
    expected = ['a', 'e', 'i', 'q', 'o', 'u']
    assert insertArrayShift(actual, to_insert) == expected
