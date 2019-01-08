# Find Edges
Given a business trip itinerary, and an Alaska Airlines route map, is the trip possible with direct flights? If so, how much will the total trip cost be?

## Challenge
Write a function based on the specifications above, which takes in a graph, and an array of city names. Without utilizing any of the built-in methods available to your language, return whether the full trip is possible with direct flights, and how much it would cost.

## Approach & Efficiency
Iterate over the list of cities up to the second-to-last. For each city, if the next city is in its adjacency list, add the edge weight to total cost. If it isn't, return (False, 0). When iteration completes, return True and total cost.

Time cost: O(n)
Storage cost: O(1)

## Solution
![solution](https://github.com/scott-currie/data_structures_and_algorithms/raw/master/assets/get_edges.jpg)
