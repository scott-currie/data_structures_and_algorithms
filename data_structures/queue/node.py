class Node(object):
    """Class representing node objects.

    """
    def __init__(self, val, _next=None):
        """Initialize a new node object with supplied value and default pointer to None.

        :param val: data value to store in the node
        :param _next: reference to the next node, defaults to None
        """
        print('val=', val)
        self.val = val
        self._next = _next

    def __repr__(self):
        """
        :return: A string representation of the Node object
        """
        return f'<Node: val = { self.val }>'

