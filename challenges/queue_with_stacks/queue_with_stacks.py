from .stack import Stack


class PseudoQueue(object):
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def __len__(self):
        return self.push_stack._size + self.pop_stack._size

    def enqueue(self, val):
        """Enqueue a new node with val in the PseudoQueue.

        Parameters:
        val (any): value to assign to newly enqueued node
        """
        # Try to move nodes from pop_stack to push_stack
        self.swap_stacks(self.pop_stack, self.push_stack)
        # Push the new node on the push_stack
        self.push_stack.push(val)
        # Return the PseudoQueue instance
        return self

    def dequeue(self):
        """Dequeue a node from the PseudoQueue and return it."""
        # Try to move nodes from push_stack to pop_stack
        self.swap_stacks(self.push_stack, self.pop_stack)
        # Pop the pop_stack and return the node
        return self.pop_stack.pop()

    @staticmethod
    def swap_stacks(s1, s2):
        """Move all nodes from s1 to s2."""
        while s1.top is not None:
            tmp_node = s1.pop()
            tmp_node._next = s2.top
            s2.top = tmp_node
