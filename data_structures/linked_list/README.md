# Linked List Insertions
Extend the LinkedList class to insert new elements at various positions.

## Challenge
- append(value) which adds a new node with the given value to the end of the list
- insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
- insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node

## Approach & Efficiency
All solutions involved traversing the list from head to tail. Storage for all methods is O(n).
- append is always O(n).
- insertBefore is worst-case O(n)
- insertAfter is worst-case O(n)


## Solution
![solution](https://github.com/scott-currie/data_structures_and_algorithms/raw/master/assets/ll_insertions_1.jpg)

![solution](https://github.com/scott-currie/data_structures_and_algorithms/raw/master/assets/ll_insertions_2.jpg)
