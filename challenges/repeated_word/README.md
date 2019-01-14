# First repeated word
Find the first repeated word in a book.

## Challenge
Write a function that accepts a lengthy string parameter.
Without utilizing any of the built-in library methods available to your language, return the first word to occur more than once in that provided string.

## Approach & Efficiency
1. Split the string into a list of words.
2. Iterate over the list. Try to add each word as a key in a hashtable.
3. If the key already exists, the word has already been seen, so return that word.
4. If the end of the word list is reached, return None. No repeated words were found.

Big O (n is number of words to check):
    Time: O(n), 
    Space: O(n)

## Solution
   - ![solution](https://github.com/scott-currie/data_structures_and_algorithms/raw/master/assets/first_repeated_word.jpg)