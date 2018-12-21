class Graph:
    """Implements a graph data type. Nodes will be represented as dict
    keys, with values stored as dicts with keys as neighboring nodes
    and values representing the edge weights.

    """
    def __init__(self):
        self.graph = {}
        self._size = 0

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __len__(self):
        pass

    def add_vert(self, val):
        """
        """
        if not self.has_vert(val):
            self.graph[val] = val
            return True
        else:
            raise KeyError('The supplied value already exists in the graph.')
        return False

    def has_vert(self, val):
        """Check if a vertex exists in the graph. This is simply
        a matter of checking whether val is a key in self.graph.

        input: val: value to search for. This is a dict key, so must be hashable.
        return: True if val is a key
        return: False if val not found
        """
        return True if val in self.graph else False


    def add_edge(self, v1, v2, weight):
        """
        """
        # add a relationship and weight between two verts
        # don't forget to validate
        pass

    def get_neighbors(self, val):
        """
        """
        # Given a val (key), return all adjacent verts
        pass
