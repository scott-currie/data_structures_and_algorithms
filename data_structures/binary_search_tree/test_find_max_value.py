from .bst import BST


def test_function_imports():
    assert BST.find_max_value


def test_fmv_empty_tree_returns_none():
    empty = BST()
    assert empty.find_max_value() is None


def test_fmv_returns_max():
    bst = BST([5, 4, 3, 6, 7])
    assert bst.find_max_value() == 7
    bst = BST([4, 3, 2, 1])
    assert bst.find_max_value() == 4
    bst = BST([7, 8, 9, 10])
    assert bst.find_max_value() == 10
