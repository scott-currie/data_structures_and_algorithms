from .breadth_first_traversal import breadth_first_traversal
from data_structures_and_algorithms.data_structures.binary_search_tree.bst import BST
import pytest


def test_imports():
    assert breadth_first_traversal
    assert BST


def test_bft(capsys):
    # bst = BST([5, 3, 2, 11, 27, 25])
    # # bst.in_order(bst.root)
    # breadth_first_traversal(bst)
    # captured = capsys.readouterr()
    # expected = '5\n3\n11\n2\n27\n25\n'
    # assert captured.out == expected
    bst = BST([2, 1, 3])
    # bst.in_order(bst.root)
    breadth_first_traversal(bst)
    captured = capsys.readouterr()
    expected = '2\n1\n3\n'
    assert captured.out == expected
