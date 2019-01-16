# Left Join Hashmaps
Implement a simplified LEFT JOIN for 2 Hashmaps.

## Challenge
- Write a function that LEFT JOINs two hashmaps into a single data structure.
- The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
- The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
- Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
- LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row. If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.
- The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic.
- Avoid utilizing any of the library methods available to your language.

## Approach & Efficiency
Iterate over all indices of hm1. If there is a node there, add its key and associated value to a list, then add the value of that key from hm2, which will be a string or None. Then append that list to a results list. Traverse child nodes if there are any and repeat the process until all nodes have been visited. Return the list.  
Time = O(n)  
Storage = O(n)


## Solution
![solution](https://github.com/scott-currie/data_structures_and_algorithms/raw/master/assets/left_join_hashmaps.jpg)
