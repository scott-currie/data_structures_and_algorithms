def depth_first(graph, root=None):
    """Perform in-order depth-first traversal on a graph.

    :input: graph: a Graph object
    :input: root: value of the root node
    :return: None
    """
    graph = graph.graph
    # Check empty graph
    if not graph:
        return []
    # root is first key in graph if not specified
    if root is None:
        root = list(graph.keys())[0]
    stack = []
    visited = []

    stack.append(root)
    while len(stack) > 0:
        # current is top of stack
        current = stack[-1]
        # Add current to visited if not already there
        if current not in visited:
            visited.append(current)
        # Add the next adjacent to the stack if not in visited
        for adj in graph[current].keys():
            if adj not in visited:
                stack.append(adj)
                # Break here to only add a single child
                break
        else:
            # Pop the stack if current had no unvisited children
            stack.pop()
    return visited
