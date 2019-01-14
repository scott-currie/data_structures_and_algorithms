# HashTable
### Author: Scott Currie
### Version: 0.1.0

## Description
Implements a hash table in Python.

## Architecture
Requires Python >= 3.6

## Methods
### get_idx
    Given a key value, turn it into an index. The string value of k is hashed using MD5, then the modulo of that int value and the table length becomes the index.

### add
    Add a key, value pair to the hash table.
    
### get
    Get the value associated with the specified key, looking at hashed index.
    
## Efficiency
### Lookups:
Time: O(1) best-case. This implementation is highly prone to hash collisions  
Space: O(1S) 
