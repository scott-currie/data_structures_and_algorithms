from node import Node
import pytest
from stack import Stack


@pytest.fixture
def short_stack(scope='function'):
    return Stack([1, 2, 3])


# Stack init

def test_stack_empty_len_zero():
    """Test if an empty stack has length == 0"""
    assert len(Stack()) == 0


def test_stack_init_list_len_3(short_stack):
    """Initialize list with iterable and test length."""
    assert len(Stack([1, 2, 3])) == 3


def test_stack_init_empty_list():
    """Test initialization with empty list."""
    assert len(Stack([])) == 0

# Stack push


def test_stack_push_increases_len(short_stack):
    """Test pushing a node increases stack length."""
    short_stack.push(-1)
    assert len(short_stack) == 4


# Stack pop

def test_stack_pop_reduces_len(short_stack):
    """Test pop actually removes a node by comparing length."""
    short_stack.pop()
    assert len(short_stack) == 2


def test_stack_pop_correct_val(short_stack):
    """Test that pop returns the correct node."""
    expected = 13
    short_stack.push(expected)
    assert short_stack.pop().val == expected

# Stack peek


def test_stack_peek_empty_stack():
    """Empty stack should return None."""
    expected = None
    assert Stack().peek() is expected


def test_stack_peek_correct_value(short_stack):
    """Test value of node returned by peek is expected."""
    expected = 3
    node = short_stack.peek()
    print(node)
    assert node.val == expected
