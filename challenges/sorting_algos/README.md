# Selection Sort
Perform a selection sort on a list.

## Challenge
Write a function that performs a selection sort. Return the modified list.

## Approach & Efficiency
- Iterate each item in the list. 
- Find the minimum value of the remaining items (all those to the right of the current item.)
- If the minimum remaining value is less than current, swap those items.
- Return the modified list. 


Time cost: O(n^2)
Storage cost: O(1), as list is sorted in place
