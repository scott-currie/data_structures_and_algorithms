# Tree Intersection
Find common values in 2 binary trees.

## Challenge
Write a function called tree_intersection that takes two binary tree parameters.
Without utilizing any of the built-in library methods available to your language, return a set of values found in both trees.

## Approach & Efficiency
1. Perform a recursive traversal over the first tree, adding each value to a set.  
    O(n) time, O(n) space
2. Perform recursive traversal over the second tree. Search for each value in the set of values from tree1.  
    O(n) time, O(n) space
3. If a value from tree2 is found in tree1, add it to an output set.
4. Return the output set.

## Solution
   - ![solution](https://github.com/scott-currie/data_structures_and_algorithms/raw/master/assets/tree_intersection.jpg)
