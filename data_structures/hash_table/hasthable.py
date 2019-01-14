import hashlib


class HashTable(object):
    def __init__(self):
        """Initialize HashTable objects. Default list size is 10.

        """
        self.table = [None for _ in range(10)]

    def __repr__(self):
        """"""
        return '<HashTable object>'

    def __str__(self):
        """

        :return:
        """
        return '{}'

    def add(self, k, v):
        """Add a new key/value pair to HashTable.

        :param k: key to add in HashTable
        :param v: value to add in HashTable
        :return: True if k, v added, else False
        """
        idx = self.get_idx(k)
        # Anything at hashed index yet?
        if self.table[idx] is not None:
            node = self.table[idx]
            while node is not None:
                if node.val[0] == k:
                    raise KeyError('The supplied key already exists.')
                if node.next is None:
                    node.next = Node((k, v))
                    return True
                node = node.next
        # Nothing at hashed index yet
        self.table[idx] = Node((k, v))
        return True

    def get_idx(self, k):
        """Hash the value of the supplied key to determine the list index to find the key.

        :param k: the key to hash
        :return: integer index of the list
        """
        hash_val = hashlib.md5(bytes(k))
        hash_int = int(hash_val.hexdigest(), 16)
        idx = hash_int % len(self.table)
        return idx

    def get(self, k):
        """Look up the index k hashes to and search it for k.

        :param k: the key to find
        :return: value associated with k
        """
        idx = self.get_idx(k)
        try:
            node = self.table[idx]
        except IndexError:
            return None
        while node is not None:
            if node.val[0] == k:
                return node.val[1]
            node = node.next
        return None

class Node(object):
    """Simple node class to populate HashTable."""
    def __init__(self, val):
        """Set up new nodes.

        :param val: value to store in the new Node
        """
        self.val = val
        self.next = None