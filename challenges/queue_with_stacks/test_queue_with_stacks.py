from .queue_with_stacks import PseudoQueue
import pytest


@pytest.fixture
def empty_queue():
    return PseudoQueue()

@pytest.fixture
def queue_of_3():
    q = PseudoQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    return q

def test_empty_queue_length_zero(empty_queue):
    assert len(empty_queue) == 0


def test_enqueue_empty_queue_accepts_val(empty_queue):
    assert empty_queue.enqueue(5)


def test_queue_has_expected_length(queue_of_3):
    assert len(queue_of_3) == 3


def test_dequeue_empty_queue_returns_None(empty_queue):
    assert empty_queue.dequeue() is None


def test_dequeue_after_queue(queue_of_3):
    queue_of_3.enqueue(4)
    assert queue_of_3.dequeue().val == 1


def test_queue_after_dequeue(queue_of_3):
    queue_of_3.enqueue(1)
    queue_of_3.enqueue(2)
    queue_of_3.enqueue(3)
    print(len(queue_of_3))
    assert queue_of_3.dequeue().val == 1
