def get_edges(graph, cities):
    """ Determine if a graph representing an airline route map and an
    itinerary list of destination cities can be completed with direct flights.
    Cities are reachable by direct flights if they share a vertex.

    :input: graph: Graph object representing the vertices and edges
    :input: cities: list of strings, representing cities
    :return: True if all cities connected by direct flights
        False if not.
    :return: int representing to sum of all edge weights between cities
    """
    graph = graph.graph
    total_cost = 0
    for i in range(len(cities) - 1):
        city1, city2 = cities[i], cities[i + 1]
        if city2 not in graph[city1].keys():
            return False, 0
        total_cost += graph[city1][city2]
    return True, total_cost
