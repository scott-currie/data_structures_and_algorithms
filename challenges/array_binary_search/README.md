# Binary Search

## Challenge
Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.

## Approach & Efficiency
The approach is to consider the range of values bounded by a left and right index. Taking the value at the middle of the range and comparing the key, move the left or right index to halve the range and repeat. If the middle value matches the key value, return that index. If the right index moves past the left index, the key value is not in the list, so exit the loop and return -1.

Worst case time performance is O(log n).
Worst case space complexity is O(1).

## Solution

![solution](https://github.com/scott-currie/data_structures_and_algorithms/raw/master/assets/array_binary_search.jpg)

