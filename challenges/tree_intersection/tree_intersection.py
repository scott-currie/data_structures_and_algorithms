from ...data_structures.binary_search_tree.bst import BST


def tree_intersection(t1, t2):
    """Compare two binary search trees and return a set containing the values that are common to both.

    args:
        t1: a BST
        t2: a BST
    returns:
        a set with values common to both trees
    """
    t1_vals = set()

    def visit_t1(node):
        if node is None:
            return
        t1_vals.add(node.val)
        if node.left is not None:
            visit_t1(node.left)
        if node.right is not None:
            visit_t1(node.right)
    visit_t1(t1.root)

    common = set()

    def visit_t2(node):
        if node is None:
            return
        if node.val in t1_vals:
            common.add(node.val)
        if node.left:
            visit_t2(node.left)
        if node.right:
            visit_t2(node.right)
    visit_t2(t2.root)

    return common




