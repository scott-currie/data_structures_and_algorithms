import pytest
from ...data_structures.binary_search_tree.bst import BST
from .tree_intersection import tree_intersection

@pytest.fixture
def balanced_tree():
    bst = BST()
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)
    bst.insert(4)
    bst.insert(5)
    return bst

@pytest.fixture
def another_tree():
    bst = BST()
    bst.insert(3)
    bst.insert(2)
    bst.insert(0)
    bst.insert(9)
    bst.insert(15)
    return bst

def test_import():
    assert BST


def test_tree_intersection(balanced_tree, another_tree):
    """Test that only values known common in both trees are in returned set."""
    assert 0 not in tree_intersection(balanced_tree, another_tree)
    assert 1 not in tree_intersection(balanced_tree, another_tree)
    assert 2 in tree_intersection(balanced_tree, another_tree)
    assert 3 in tree_intersection(balanced_tree, another_tree)
    assert 4 not in tree_intersection(balanced_tree, another_tree)
    assert 5 not in tree_intersection(balanced_tree, another_tree)
    assert 9 not in tree_intersection(balanced_tree, another_tree)
    assert 15 not in tree_intersection(balanced_tree, another_tree)


def test_tree_intersection_no_common(balanced_tree):
    """Set returned when trees have no common values should have length 0."""
    other_tree = BST([11, 7, 15, 9, 13])
    assert len(tree_intersection(balanced_tree, other_tree)) == 0
