from .stack import Stack


class PseudoQueue(object):
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def __len__(self):
        return self.push_stack._size + self.pop_stack._size

    def enqueue(self, val):
        """Enqueue a new node with val in the PseudoQueue."""
        # Try to move nodes from pop_stack to push_stack
        while self.pop_stack.top is not None:
            self.push_stack.push(self.pop_stack.pop())
        # Push the new node on the push_stack
        self.push_stack.push(val)
        # Return the PseudoQueue instance
        return self

    def dequeue(self):
        """Dequeue a node from the PseudoQueue and return it."""
        # Try to move nodes from push_stack to pop_stack
        while self.push_stack.top is not None:
            self.pop_stack.push(self.push_stack.pop().val)
        # Pop the pop_stack and return the node
        return self.pop_stack.pop()
