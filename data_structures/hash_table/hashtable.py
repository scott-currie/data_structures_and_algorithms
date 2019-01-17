import decimal, hashlib


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

    def set(self, k, v):
        """Assign a key/value pair in the HashTable. Create a new pair if the key doesn't already exsist. If the key
        exists, update its associated value.

        :param k: key to set/add in HashTable
        :param v: value to assign in HashTable
        :return: True if k, v added, else False
        """
        idx = self.get_idx(k)
        # Anything at hashed index yet?
        if self.table[idx] is not None:
            node = self.table[idx]
            while node is not None:
                if node.val[0] == k:
                    # raise KeyError('The supplied key already exists.')
                    node.val = (k, v)
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
        hashables = [int, float, decimal, complex, bool, str, tuple, range, frozenset, bytes]
        if type(k) not in hashables:
            raise TypeError('Key must be of type: int, float, decimal, complex, bool, str, tuple, range, frozenset, bytes')
        if not isinstance(k, str):
            k = str(k)
        hash_val = hashlib.md5(bytes(k, encoding='UTF-8'))
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

    def remove(self, k):
        """Remove the key, value pair with specified key.

        :param k: key to search for
        :return: True if key found and removed, else False
        """
        node = self.table[self.get_idx(k)]
        print('Looking for {}'.format(k) )
        print(node.val)
        if node.val[0] == k:
            print('Found {}'.format(k))
            # unlink this node. If it is the only value here, set table at that index to None
            if node.next is None:
                self.table[self.get_idx(k)] = None
        while node.next is not None:
            if node.next.val[0] == k:
                if node.next.next is None:
                    node.next = None
                else:
                    node.next = node.next.next

class Node(object):
    """Simple node class to populate HashTable."""
    def __init__(self, val):
        """Set up new nodes.

        :param val: value to store in the new Node
        """
        self.val = val
        self.next = None
