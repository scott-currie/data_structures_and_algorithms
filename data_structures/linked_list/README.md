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

# kth From End
Extend the LinkedList class to find the value of the node k nodes from the end.

## Challenge
Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach & Efficiency
Iterate over the list once to accumulate a node count. Iterate over the list length - k times, then return the value of current at that time.
Time = O(2n) worst case
Storage = O(n)


## Solution
![solution](https://github.com/scott-currie/data_structures_and_algorithms/raw/master/assets/ll_kth_from_end.jpg)

![solution](https://github.com/scott-currie/data_structures_and_algorithms/raw/master/assets/ll_insertions_2.jpg)
