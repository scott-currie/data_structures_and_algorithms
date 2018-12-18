def fizz_buzz_tree(tree):
    """Traverse a tree and modify node values based on fizz-buzz
    rules.

    input: tree(binary tree): Tree to modify
    return: binary tree: Modified tree
    """
    in_order_traverse(tree.root)
    return tree


def in_order_traverse(root):
    """Traverse a tree in order starting with root.

    input: root(Node): starting node
    return: None
    """
    if not root:
        return
    if root.left:
        in_order_traverse(root.left)
    fizz_buzz(root)
    if root.right:
        in_order_traverse(root.right)


def fizz_buzz(node):
    """Modify node value based on fizz-buzz rules.

    input: node (Node): node to modify
    return: None
    """
    val = ''
    if node.val % 3 == 0 and node.val % 5 == 0:
        val = 'FizzBuzz'
    elif node.val % 3 == 0:
        val = 'Fizz'
    elif node.val % 5 == 0:
        val = 'Buzz'
    node.val = val if val else node.val
