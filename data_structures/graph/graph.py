class Graph:
    """Implements a graph data type. Nodes will be represented as dict
    keys, with values stored as dicts with keys as neighboring nodes
    and values representing the edge weights.
    """

    def __init__(self):
        self.graph = {}

    def __repr__(self):
        return f'<Graph object: size={ len(self.graph) }>'

    def __str__(self):
        return f'Graph: { len(self.graph) }'

    def __len__(self):
        return len(self.graph)

    def add_vert(self, val):
        """Add a vertex to the graph with supplied val. The vertex will be initialized
        with an empty adjacency list and no edges.

        input: val : value to serve as the vertex. This is a dict key, so an exception will be
        be raised if it is not hashable
        return: self
        """
        # Check if the supplied value is a valid dict key
        try:
            {val: 0}
        except TypeError:
            raise TypeError('Vertex values must be hashable types.')
        if not self.has_vert(val):
            self.graph[val] = {}
        else:
            raise KeyError('The supplied value already exists in the graph.')
        return self

    def has_vert(self, val):
        """Check if a vertex exists in the graph. This is simply
        a matter of checking whether val is a key in self.graph.

        input: val: value to search for. This is a dict key, so must be hashable.
        return: True if val is a key
        return: False if val not found
        """
        return True if val in self.graph else False

    def add_edge(self, v1, v2, weight):
        """Add an edge with supplied weight between two vertices. Both vertices
        must exist in the graph, and an existing edge between them must not
        already exist.

        input: v1, vertex to serve as starting point
        input: v2, vertex to serve as end point
        weight: int, weight to apply to the edge
        return: True if edge was added successfully
        return: False if edge add failed
        """
        # Ensure both vertices exist
        if self.has_vert(v1) and self.has_vert(v2):
            # Ensure the edge doesn't already exist
            if v2 not in self.graph[v1]:
                self.graph[v1][v2] = weight
                return True
        return False

    def get_neighbors(self, val):
        """Find all of the neighbors of the vertex with supplied val.

        input: val, value of the starting vertex
        return: tuple representing all the values of adjacent vertices
        """
        if self.has_vert(val):
            return tuple(n for n in self.graph[val])
