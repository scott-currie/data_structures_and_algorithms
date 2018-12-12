# Multi-Bracket Validation

## Challenge
Write a function multi_bracket_validation that takes a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets: {}, (), []

## Approach & Efficiency
Create a stack. Iterate over ever character in the string. If it's an opener, push it on the stack. If it's a closer, peek the stack and compare values. If they're opposites, pop the stack and keep going. If they're not, immediately return False. After iterating the entire string, return True if the stack is empty, else return False.

Efficiency: Time = O(n), Storage (worst-case) = O(n)

## Solution

![solution](https://github.com/scott-currie/data_structures_and_algorithms/raw/master/assets/multi_bracket_validation.jpg)

