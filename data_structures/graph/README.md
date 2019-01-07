# Graph
### Author: Scott Currie
### Version: 0.1.0

# Description
An implementation of a directed, weighted graph datastructure in Python. The graph is represented as a dictionary whose keys are the values of the vertices. The values are dictionaries whose keys represent adjacent nodes, and their values are numbers representing the weights of the edges.

# Architecture
Requires Python >= 3.6

# Methods
- ## Breadth first traversal: perform a breadth first traversal over the graph. Return a list of nodes in the order they were visited.
    - ### Approach: Create a queue to hold nodes to visit and a list to hold nodes as they are visited. Enqueue the first node and its neighbors. While the queue is not empty repeat the following:
    1. Dequeue and add it to visited.
    2. For each adjacent node, if it isn't already visited, add it to the queue.
    - ### Efficiency:
        - Time O(n)
        - Space O(2n)
    - ### Solution:
    - ![solution](https://github.com/scott-currie/data_structures_and_algorithms/raw/master/assets/breadth_first_graph.jpg)

