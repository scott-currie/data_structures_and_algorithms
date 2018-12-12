class Node(object):
    """Node object suitable for inclusion in singly linked list, consisting of a value and a reference to the next node.
    """
    def __init__(self, val, _next=None):
        self.val = val
        self._next = _next

    def __str__(self):
        output = f'{ self.val }'
        return output
