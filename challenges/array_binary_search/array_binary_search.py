def binary_search(search_list, search_key):
    """Find the index of a value of a key in a list usings a
    binary search algorithg. Returns the index of the value if
    found. Otherwise, returns -1.
    """
    left_idx, right_idx = 0, len(search_list) - 1
    # while True:
    while left_idx <= right_idx:
        mid_idx = (right_idx + left_idx) // 2
        # search_key is left of middle value
        if search_key < search_list[mid_idx]:
            right_idx = mid_idx - 1
        # search key is right of middle value
        elif search_key > search_list[mid_idx]:
            left_idx = mid_idx + 1
        else:
            return mid_idx
    # If we get here, the value was not found.
    return -1


if __name__ == '__main__':
    binary_search([1, 2, 3], 4) == -1
