from .node import Node


class Stack(object):
    """Class to implement stack functionality. It serves as a wrapper for
    Node objects and implements push, pop, and peek functionality. It also
    overrides __len__ to return a _size attribute that should be
    updated by any method that adds or removes nodes from the stack.
    """

    def __init__(self, _iterable=None):
        """Initialize a stack.

        param: _iterable: Optional list that can be used to seed the stack.
        """
        self.top = None
        self._size = 0

        if not _iterable:
            _iterable = []

        if type(_iterable) is not list:
            raise TypeError('Iterable must be list type.')

        for value in _iterable:
            self.push(value)

    def __len__(self):
        """Override __len__ builtin to return _size. Methods extending the class
        that push or pop nodes need to update _size accordingly.

        return: _size: an int representing the number of nodes in the stack
        """
        return self._size

    def push(self, val):
        """Create a new node with data value and push onto stack."""
        node = Node(val)
        node._next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        """Remove the top node from the stack and return it.

        return: Node object that was previously top of the stack
        """
        if self.top:
            node = self.top
            self.top = node._next
            self._size -= 1
            return node
        return None

    def peek(self):
        """Return the top node.

        return: Node object that is currently top of the stack
        """
        if self.top:
            return self.top
        return None
