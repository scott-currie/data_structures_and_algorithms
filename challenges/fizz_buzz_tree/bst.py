class Node(object):
    """Simple node object suitable for binary tree.
    """

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        """Implement __repr__ to show val of current, left child and right child."""
        return f'<Node object: val={self.val} left={ self.left } right={ self.right }>'

    def __str__(self):
        """Return string value of node value."""
        return str(self.val)


class BST(object):
    """Implements a binary search tree of Node instances.

    """

    def __init__(self, it=None):
        """Initialize tree an empty tree or populate with an iterable.

        input: it(iterable): optional, can be used to populate the tree on init
        """
        self.root = None
        self._size = 0
        if it:
            for item in it:
                self.insert(item)

    def __len__(self):
        """Implement __len__ for BST class."""
        return self._size

    def pre_order(self, node=None, operation=lambda x: print(x)):
        """Perform pre-order traversal of nodes. Recursively calls pre_order on the
        current node until None is reached, then returns down the stack to the next valid
        node.

        input: node(Node): optional. The current node in the traversal.
        input: operation(function): optional. The operation to perform on nodes.
        return: None
        """
        if node is None:
            return

        operation(node)

        if node.left is not None:
            self.pre_order(node.left)
        if node.right is not None:
            self.pre_order(node.right)

    def post_order(self, node=None, operation=lambda x: print(x)):
        """Perform post-order traversal of nodes. Recursively calls post_order on the
        current node until None is reached, then returns down the stack to the next valid
        node.
    
        input: node(Node): optional. The current node in the traversal.
        input: operation(function): optional. The operation to perform on nodes.
        return: None 
        """
        if node is None:
            return
        if node.left:
            self.post_order(node.left)
        if node.right:
            self.post_order(node.right)
        operation(node)

    def in_order(self, node=None, operation=lambda x: print(x)):
        """Perform in-order traversal of nodes. Recursively calls in_order on the
        current node until None is reached, then returns down the stack to the next valid
        node.

        input: node(Node): optional. The current node in the traversal.
        input: operation(function): optional. The operation to perform on nodes.
        return: None
        """
        if node is None:
            return
        if node.left:
            self.in_order(node.left)
        operation(node)
        if node.right:
            self.in_order(node.right)

    def insert(self, val):
        """Insert a new node with val. If there's no root, it's the root. Else find
        a place to put it. Duplicate values insert to the left."""
        node = Node(val)
        if self.root is None:
            self.root = node
            self._size += 1
            return self._size
        current = self.root
        while True:
            # New node val lt current
            if node.val <= current.val:
                # Is there a left child? Follow it.
                if current.left:
                    current = current.left
                # No left child? New node is left child
                else:
                    current.left = node
                    self._size += 1
                    return self._size
            if node.val > current.val:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    self._size += 1
                    return self._size
