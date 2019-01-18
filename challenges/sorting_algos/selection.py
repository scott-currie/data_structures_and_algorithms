def selection_sort(lst):
    """Perform an in-place selection sort on a list.

    params:
        lst: list to sort
    returns:
        lst: passed in sequence in sorted order
    """
    if not isinstance(lst, list):
        raise TypeError('Sequence to be sorted must be list type.')
    for i in range(len(lst) - 1):
        min_idx =  i + 1
        for j in range(min_idx, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        if lst[min_idx] < lst[i]:
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

