from node import Node
import pytest
from queue import Queue


@pytest.fixture()
def short_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    return q


# enqueue


def test_queue_queue_increased_len():
    """Enqueue a value and check the length of the queue increased by 1"""
    q = Queue()
    assert len(q) == 0
    q.enqueue(1)
    assert len(q) == 1


def test_queue_bad_value_exception(short_queue):
    """enqueue(None) shoud raise an exception"""
    q = Queue()
    with pytest.raises(ValueError):
        q.enqueue(None)


# dequeue


def test_dequeue_empty_is_none():
    """dequeue on empty queue should return None"""
    q = Queue()
    assert q.dequeue() is None


def test_dequeue_decreased_len(short_queue):
    q = short_queue
    assert len(q) == 3
    node = q.dequeue()
    assert len(q) == 2


def test_dequeue_val_is_expected(short_queue):
    """val of dequeued node should match expected."""
    node = short_queue.dequeue()
    assert node.val == 1


def test_queue_queue_val_expected():
    """val of queued node is expected"""
    expected = 9
    q = Queue()
    q.enqueue(expected)
    assert q.dequeue().val == expected


def test_multiple_dequeue(short_queue):
    """Dequeue all nodes in queue and test their values."""
    assert short_queue.dequeue().val == 1
    assert short_queue.dequeue().val == 2
    assert short_queue.dequeue().val == 3
    assert short_queue.dequeue() is None
