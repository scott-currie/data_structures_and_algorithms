from queue import Queue


class Node(object):
    """"""

    def __init__(self, val):
        """"""
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        """"""
        return f'<Node object: val={ self.val }>'

    def __str__(self):
        """"""
        return str(self.val)


class BinaryTree(object):
    """"""

    def __init__(self, it=None):
        """"""
        self.root = None
        if it:
            for el in it:
                self.insert(el)

    def __repr__(self):
        """"""
        pass

    def __str__(self):
        """"""
        pass

    def insert(self, val):
        """Insert a new node with supplied value in the first open position, following
        breadth-first traversal order.
        """
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return
        q = Queue()
        q.put(self.root)
        while q.full():


    def breadth_first(self, func=lambda x: print(x)):
        if self.root is None:
            print('No root.')
            return
        q = Queue()
        q.put(self.root)
        while not q.empty():
            curr = q.get()
            # print(curr)
            if curr.left:
                q.put(q.left)
            if curr.right:
                q.put(q.right)
            func(curr)
            # print(curr.val)
