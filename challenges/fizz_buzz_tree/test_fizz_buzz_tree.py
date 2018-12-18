from .bst import BST
from .fizz_buzz_tree import fizz_buzz_tree
import pytest


@pytest.fixture
def all_fizz():
    bst = BST([9, 6, 3, 18, 27])
    return bst


@pytest.fixture
def all_buzz():
    bst = BST([20, 10, 5, 25, 35])
    return bst


def test_fbt_all_fizz(capsys, all_fizz):
    all_fizz = fizz_buzz_tree(all_fizz)
    all_fizz.in_order(all_fizz.root)
    captured = capsys.readouterr()
    expected = 'Fizz\nFizz\nFizz\nFizz\nFizz\n'
    assert captured.out == expected


def test_fbt_all_buzz(capsys, all_buzz):
    all_buzz = fizz_buzz_tree(all_buzz)
    all_buzz.in_order(all_buzz.root)
    captured = capsys.readouterr()
    expected = 'Buzz\nBuzz\nBuzz\nBuzz\nBuzz\n'
    assert captured.out == expected


def test_fbt_mixed_cases(capsys):
    bst = BST([5, 3, 2, 11, 15])
    bst = fizz_buzz_tree(bst)
    bst.in_order(bst.root)
    captured = capsys.readouterr()
    expected = '2\nFizz\nBuzz\n11\nFizzBuzz\n'
    assert captured.out == expected
    bst = BST([27, 15, 18, 3, 64, 75, 50])
    bst = fizz_buzz_tree(bst)
    bst.in_order(bst.root)
    captured = capsys.readouterr()
    expected = 'Fizz\nFizzBuzz\nFizz\nFizz\nBuzz\n64\nFizzBuzz\n'
    assert captured.out == expected

def test_fbt_no_modfications(capsys):
    bst = BST([4, 2, 1, 7, 11, 8])
    fizz_buzz_tree(bst)
    bst.in_order(bst.root)
    captured = capsys.readouterr()
    expected = '1\n2\n4\n7\n8\n11\n'
    assert captured.out == expected
