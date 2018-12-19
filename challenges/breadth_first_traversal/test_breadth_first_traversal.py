from .breadth_first_traversal import breadth_first_traversal
from data_structures_and_algorithms.data_structures.binary_search_tree.bst import BST


def test_imports():
    assert breadth_first_traversal
    assert BST


def test_bft(capsys):
    """Test breadth_first_traversal function with some test trees
    and compare captured stdout with expected values."""
    bst = BST([2, 1, 3])
    breadth_first_traversal(bst)
    captured = capsys.readouterr()
    expected = '2\n1\n3\n'
    assert captured.out == expected
    bst = BST([3, 2, 1])
    breadth_first_traversal(bst)
    captured = capsys.readouterr()
    expected = '3\n2\n1\n'
    assert captured.out == expected
    bst = BST([1, 2, 3])
    breadth_first_traversal(bst)
    captured = capsys.readouterr()
    expected = '1\n2\n3\n'
    assert captured.out == expected
    bst = BST([2, 1, 3, 4])
    breadth_first_traversal(bst)
    captured = capsys.readouterr()
    expected = '2\n1\n3\n4\n'
    assert captured.out == expected
