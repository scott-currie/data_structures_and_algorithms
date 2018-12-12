from .queue import Queue


class AnimalShelter(Queue):
    def __init__(self):
        self.__super__()

    def get_pet(self, pet):
        """Find the node closest to the front of the queue that represents a pet of the specified type.

        param: pet (str): target value to find
        return: (Node): node removed from queue
        return: (None): if target pet was not found
        """
        current = self.rear
        pets = 0
        # Traverse queue to count matching pets
        while current is not None:
            pets += 1 if current.val == pet else 0
        # No matching pets found. Return None.
        if pets == 0:
            return None
        # Do it again
        current = self.rear
        if current.val != pets:
            current = current._next
        else:
            val -= 1
            if val == 0:

