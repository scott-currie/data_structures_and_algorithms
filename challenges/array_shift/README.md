# Insert and shift middle index of array

## Challenge
Write a function called insertShiftArray which takes in an array and the value to be added. Return an array with the new value added at the middle index.

## Approach & Efficiency
I found the middle index by dividing the length of the list by 2, then got the ceiling of the result. I sliced the list up to that index, then added a list with the new value as its only element, then added the slice of the list starting with the middle index to the end.

    left_slice + [value] + right_slice

The solution is O(n) for time and storage. Both increase in a linear manner as the number of list items grows.

## Solution

