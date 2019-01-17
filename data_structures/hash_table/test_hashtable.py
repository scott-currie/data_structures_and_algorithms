from .hashtable import HashTable
import pytest


def test_import():
    assert HashTable
    assert HashTable()

def test_add_new_key():
    """Test adding a valid entry that doesn't already exist."""
    ht = HashTable()
    assert ht.set(0, 1) == True
    assert ht.set('0', 1) == True
    assert ht.set((0, 0), 1) == True

def test_add_existing_key():
    """Test adding a valid entry that already exists."""
    ht = HashTable()
    ht.set(0,1)
    assert ht.get(0) == 1
    ht.set(0, 3)
    assert ht.get(0) == 3

def test_add_invalid_type():
    """Test adding an item with an invalid key."""
    ht = HashTable()
    with pytest.raises(TypeError):
        ht.set([1, 2, 3], 9)

def test_get_valid_key():
    """Test existing key returns expected value."""
    ht = HashTable()
    ht.set(0, 1)
    assert ht.get(0) == 1

def test_get_invalid_key():
    """Test that getting a nonexistent key returns None."""
    ht = HashTable()
    ht.set(0, 1)
    assert ht.get(1) is None

def test_get_idx_collision():
    """Test that two keys that hash to the same value return same index."""
    ht = HashTable()
    assert ht.get_idx(4) == ht.get_idx(36)

def test_get_key_collision():
    """Test that two keys that hash to the same value are retrieved successfully."""
    ht = HashTable()
    ht.set(4, 'four')
    ht.set(36, 'thirty-six')
    assert ht.get(4) == 'four'
    assert ht.get(36) == 'thirty-six'

def test_remove_key_collision():
    """Test that two keys that hash to the same value are retrieved successfully."""
    ht = HashTable()
    ht.set(4, 'four')
    ht.set(36, 'thirty-six')
    assert ht.get(4) == 'four'
    assert ht.get(36) == 'thirty-six'
    ht.remove(36)
    assert ht.get(36) is None
