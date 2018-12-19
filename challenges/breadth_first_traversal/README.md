# Breadth First Traversal
## Challenge
Write a function that accepts a tree and traverses all nodes in breadth first order, printing the value of each node visited.

## Approach & Efficiency
The function uses a queue to keep track of nodes visited. Enqueue the first node, then while the queue is not empty, dequeue the front node, enqueue its left child, if any, print its value, and enqueue its right child, if any.

Time: O(n) due to always having to visit every node.
Storage: O(n) worst case since we have to store nodes in a queue

## Solution

![solution](https://github.com/scott-currie/data_structures_and_algorithms/raw/master/assets/breadth_first_traversal.jpg)

