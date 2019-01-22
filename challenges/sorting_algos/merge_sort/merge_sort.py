def merge(ll, rl):
    """Merge two lists.

    :param ll: left list
    :param rl: right list
    :return: new list with ll and rl in ascending order.
    """
    merged = []
    l_idx, r_idx = 0, 0
    while l_idx < len(ll) or r_idx < len(rl):
        if l_idx < len(ll):
            # Right index reached the end or left item is lower
            if r_idx >= len(rl) or ll[l_idx] <= rl[r_idx]:
                merged.append(ll[l_idx])
                l_idx += 1
        if r_idx < len(rl):
            # Left index reached end or right item is lower
            if l_idx >= len(ll) or rl[r_idx] <= ll[l_idx]:
                merged.append(rl[r_idx])
                r_idx += 1
    # print('merged:', merged)
    return merged


def merge_sort(lst):
    """Perform recursive merge sort on list. Return new list in sorted order.

    :param lst: list to sort
    :return: new sorted list
    """
    if len(lst) < 2:
        return lst
    l_sublist = lst[:len(lst) // 2]
    r_sublist = lst[len(lst) // 2:]
    ll = merge_sort(l_sublist)
    rl = merge_sort(r_sublist)
    return merge(ll, rl)
