import math


def insertArrayShift(input_list, val):
    """Takes a list and a value and returns a new list with the value inserted at the middle index.
    The input list is sliced into its left half, then the value is appended, then the right half is
    added to the end.
    """
    mid = math.ceil(len(input_list) / 2)
    return input_list[:mid] + [val] + input_list[mid:]
