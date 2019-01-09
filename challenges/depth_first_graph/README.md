# Depth First Traversal
Conduct a depth first preorder traversal on a graph

## Challenge
Create a function that accepts an adjacency list as a graph, and conducts a depth first traversal. Without utilizing any of the built-in methods available to your language, return a collection of nodes in their pre-order depth-first traversal order.

## Approach & Efficiency
The solution implements a stack and a list to track nodes to visit and already visisted. The root node is pushed to the stack. While the stack is not empty, repeat:
1. Add the top of the stack to the visited list
2. If the node on the stack has children that aren't in the visited list, add the next one to the stack.
3. If the node on the stack has no unvisited children, pop it off.

Time: O(n)
Storage: O(n)

## Solution
![solution](https://github.com/scott-currie/data_structures_and_algorithms/raw/master/assets/depth_first_graph.jpg)
