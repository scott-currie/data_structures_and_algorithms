import pytest

from bst import BST


@pytest.fixture
def balanced_tree():
    bst = BST()
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)
    bst.insert(4)
    bst.insert(5)
    return bst


def test_insert_increases_len():
    bst = BST()
    bst.insert(2)
    assert len(bst) == 1
    bst.insert(3)
    assert len(bst) == 2
    bst.insert(1)
    assert len(bst) == 3


def test_preorder_traversal_1(capsys):
    bst = BST([1, 2, 3, 4, 5])
    bst.pre_order(bst.root)
    captured = capsys.readouterr()
    assert captured.out == '1\n2\n3\n4\n5\n'


def test_preorder_traversal_2(capsys):
    bst = BST([6, 4, 3, 5, 8, 9, 7])
    bst.pre_order(bst.root)
    captured = capsys.readouterr()
    assert captured.out == '6\n4\n3\n5\n8\n7\n9\n'


def test_in_order_traversal(capsys, balanced_tree):
    balanced_tree.in_order(balanced_tree.root)
    captured = capsys.readouterr()
    assert captured.out == '1\n2\n3\n4\n5\n'


def test_inorder_traversal_2(capsys):
    bst = BST([6, 4, 3, 5, 8, 9, 7])
    bst.in_order(bst.root)
    captured = capsys.readouterr()
    assert captured.out == '3\n4\n5\n6\n7\n8\n9\n'


def test_post_order_traversal(capsys, balanced_tree):
    balanced_tree.post_order(balanced_tree.root)
    captured = capsys.readouterr()
    assert captured.out == '1\n2\n5\n4\n3\n'


def test_postorder_traversal_2(capsys):
    bst = BST([6, 4, 3, 5, 8, 9, 7])
    bst.post_order(bst.root)
    captured = capsys.readouterr()
    assert captured.out == '3\n5\n4\n7\n9\n8\n6\n'
