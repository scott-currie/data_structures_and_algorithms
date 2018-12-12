from .queue import Queue


class AnimalShelter(Queue):
    def __init__(self):
        super().__init__()

    def dequeue(self, pref):
        """Override dequeue function of Queue class. Dequeue the nodes until
        the node with value matching pref is found.

        return: node closest to front with value pref, None if queue is empty
        """
        self.print_values()
        print('Dequeue', pref, '\n')
        if pref not in ['dog', 'cat']:
            return None
        found_pet = None
        tmp_stack = None
        while self.front:

            # Front is node we want
            if self.front.val == pref:
                # Dequeue it and keep a reference
                found_pet = self.front
                self.front = self.front._next
                self._size -= 1
                # Put the tmp_stack back on the queue if anything is there
                if tmp_stack:
                    while tmp_stack._next:
                        # Get a reference to top of tmp_stack
                        tmp_node = tmp_stack
                        # Move top of tmp_node down
                        tmp_stack = tmp_stack._next
                        # Link tmp_node to queue
                        tmp_node._next = self.front
                        # Point front at tmp_node
                        self.front = tmp_node
                        self._size += 1
                break
            else:
                # Get a reference to front node
                tmp_node = self.front
                # Move front node back
                self.front = self.front._next
                self._size -= 1
                # Link tmp_node to tmp_stack
                tmp_node._next = tmp_stack
                # Point tmp_stack to new top node
                tmp_stack = tmp_node
        self.print_values()
        return found_pet if found_pet else None

    def print_values(self):
        current = self.back
        while current:
            print(current.val)
            current = current._next
