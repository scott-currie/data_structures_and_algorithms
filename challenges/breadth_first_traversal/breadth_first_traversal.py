from data_structures_and_algorithms.data_structures.queue.queue import Queue


def breadth_first_traversal(tree):
    """Perform a breadth first search on a binary tree and print the value
    of each node in order.

    input: tree(BST) tree of Node objects to traverse
    return: None
    """
    q = Queue()
    q.enqueue(tree.root)
    while len(q) > 0:
        # Reference val here to get the tree node out of the queue node
        node = q.dequeue().val
        if node.left:
            q.enqueue(node.left)
        print(node.val)
        if node.right:
            q.enqueue(node.right)
