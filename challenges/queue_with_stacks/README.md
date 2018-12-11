# Queue with Stacks

## Challenge
Implement a queue using two stacks, including enqueue and dequeue functions.

## Approach & Efficiency
One stack is for pushing (enqueuing) new nodes. Its top represents the back of the queue. The other stack is for popping (dequeuing) nodes. Its top represents the front of the queue. Enqueuing or dequeuing nodes take O(1) time if the nodes are already on the correct stack, since the needed elements are already at the top. Worst case time is O(n) if the nodes have to be moved one by one to the correct stack. Nodes are moved by reassigning pointers, so memory is O(1).

## Solution

![solution](https://github.com/scott-currie/data_structures_and_algorithms/raw/master/assets/queue_with_stacks.jpg)

