from .hashtable import HashTable
import pytest


def test_import():
    assert HashTable
    assert HashTable()

def test_add_new_key():
    """Test adding a valid entry that doesn't already exist."""
    ht = HashTable()
    assert ht.add(0, 1) == True

def test_add_existing_key():
    """Test adding a valid entry that already exists."""
    ht = HashTable()
    ht.add(0,1)
    with pytest.raises(KeyError):
        ht.add(0, 1)

def test_get_valid_key():
    """Test existing key returns expected value."""
    ht = HashTable()
    ht.add(0, 1)
    assert ht.get(0) == 1

def test_get_invalid_key():
    """Test that getting a nonexistent key returns None."""
    ht = HashTable()
    ht.add(0, 1)
    assert ht.get(1) is None

def test_get_idx_collision():
    """Test that two values return same index after hashing."""
    ht = HashTable()
    assert ht.get_idx(4) == ht.get_idx(36)

def test_get_key_collision():
    """Test that two keys that hash to the same value are retrieved successfully."""
    ht = HashTable()
    ht.add(4, 'four')
    ht.add(36, 'thirty-six')
    assert ht.get(4) == 'four'
    assert ht.get(36) == 'thirty-six'
