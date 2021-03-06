from .node import Node


class Queue(object):
    """Implements a queue."""

    def __init__(self, _iterable=None):
        self.front = None
        self.back = None
        self._size = 0

        if _iterable:
            if type(_iterable) is list:
                for value in _iterable:
                    self.enqueue(val)
            else:
                raise TypeError('Iterable must be list type.')

    def __repr__(self):
        """
        """
        return f'< Queue object: length = {self._size}'

    def __len__(self):
        """
        """
        return self._size

    def enqueue(self, value):
        """Add a new node to the back of the queue with value of value.
        """
        if value is None:
            raise ValueError('Node value cannot be None')
            return
        node = Node(value)
        if self.back:
            self.back._next = node
            self.back = self.back._next
        else:
            self.back = node
            self.front = node
        self._size += 1

    def dequeue(self):
        """Remove the node at the front of the list and return it.
        .
        return: node that was currently in front, None if queue is empty
        """
        node = self.front
        if self.front:
            self.front = self.front._next
            self._size -= 1
            if self._size == 0:
                self.front = None
                self.back = None
        return node
