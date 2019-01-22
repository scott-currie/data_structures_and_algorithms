# Merge Sort
Implement Mergesort.

## Challenge
Write a function that accepts an array of unsorted integers, and returns a sorted array by a recursive mergesort algorithm.  

## Approach & Efficiency
- Recursively split the input list in half until only 2 elements remain, then return
- Merge the two returned lists such that elements in both lists are added to a third list in ascending order.
- The resulting merged list contains all the input elements in ascending order.


Time cost: O(n * log(2)n)
Storage cost: O(n)
