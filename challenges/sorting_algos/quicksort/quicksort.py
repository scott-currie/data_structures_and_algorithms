def quicksort(s, low_idx=None, high_idx=None):
    """Perform quicksort on an iterable sequence in place.

    :param s: the sequence to sort
    :return: the passed-in sequence in sorted order.
    """
    if low_idx is None:
        low_idx = 0
    if high_idx is None:
        high_idx = len(s) - 1
    if low_idx < high_idx:
        p = partition(s, low_idx, high_idx)
        quicksort(s, low_idx, p - 1)
        quicksort(s, p + 1, high_idx)
    return s


def partition(s, low_idx, high_idx):
    pivot = s[high_idx]
    i = low_idx
    for j in range(low_idx, high_idx):
        if s[j] < pivot:
            s[i], s[j] = s[j], s[i]
            i += 1
    s[i], s[high_idx] = s[high_idx], s[i]
    return i