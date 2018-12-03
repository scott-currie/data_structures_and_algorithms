from node import Node


class LinkedList(object):
    """Implements a singly linked list in Python.
    """

    def __init__(self, iterable=None):
        self.head = None
        self._size = 0

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('iterable must be of type list')

        for val in iterable:
            self.insert(val)

    def __str__(self):
        """Override __str__ to mimic behavior of list.__str__."""
        # output = f'Linked List: Head val - { self.head }'"""
        if self._size == 0:
            return '[]'
        current = self.head
        output = '['
        while current._next:
            output += str(current.val) + ', '
            current = current._next
        output += str(current.val) + ']'
        return output

    def __repr__(self):
        output = f'<LinkedList: head - { self.head } size - { self._size }>'
        return output

    def __len__(self):
        return self._size

    def insert(self, value):
        """Insert a new node at the head of the LinkedList.

        input: (any type) value of the new node
        returns: none
        """
        node = Node(value)
        node._next = self.head
        self.head = node
        # self.head = Node(value, self.head)
        self._size += 1

    def includes(self, search_val):
        """Instance method on LinkedList. Traverse LL comparing each node's value to search_val.

        input: (any type) value to find
        returns: (boolean) True if search_val found, else False
        """
        cur = self.head
        while cur is not None:
            if cur.val == search_val:
                return True
            else:
                cur = cur._next
        return False

    def append(self, val):
        """Instance method on LinkedList. Add a new node with value val at the end of the list.

        input: val (any type) value of new node
        returns: none
        """
        current = self.head
        while current._next:
            current = current._next
        current._next = Node(val)
        self._size += 1

    def insert_before(self, val, newVal):
        """Instance method on LinkedList. Add a new node with value newVal immediately before node with value val.

        input: val (any type) value to find in the list
        input: newVal (anyType) value to insert into list
        returns: none
        """
        current = self.head
        # Handle value of current node is val
        if current.val == val:
            self.insert(newVal)
            return
        while current._next:
            print(current._next.val)
            if current._next.val == val:
                print('Found it.')
                new_node = Node(newVal, current._next)
                current._next = new_node
                self._size += 1
                return
            else:
                current = current._next

    def insert_after(self, val, newVal):
        """Instance method on LinkedList. Add a new node with value newVal immediately after node with value val.

        input: val (any type) value to find in the list
        input: newVal (anyType) value to insert into list
        returns: none
        """
        current = self.head
        while current._next:
            if current.val == val:
                new_node = Node(newVal, current._next)
                current._next = new_node
                self._size += 1
                return
            current = current._next
