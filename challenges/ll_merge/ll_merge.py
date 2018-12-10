from .linked_list import LinkedList


def ll_merge(ll1, ll2):
    """Merge two linked lists of arbitrary size, starting with the first node
    of the first list passed in and alternating through all remaining nodes
    in both lists.

    Parameters:
        ll1 (LinkedList): starting list to merge
        ll2 (LinkedList): second list to merge

    Returns:
        (LinkedList): new list with elements from both lists merged
    """
    merged = LinkedList()
    c1 = ll1.head
    c2 = ll2.head

    while c1 or c2:
        if c1:
            # If merged head is None, it's our first pass
            if merged.head is not None:
                # Next of mc is ll1 head
                mc._next = c1
                # Move mc to its next
                mc = mc._next
                # Move c1 to its next
                c1 = c1._next
                merged._size += 1
            # Not our first pass
            else:
                # If this list has reached the end, c1 is None
                if c1 is not None:
                    # Merged head is ll1 head
                    merged.head = c1
                    # mc is merged head
                    mc = merged.head
                    # Move current of ll1 to its next
                    c1 = c1._next
                    merged._size += 1
        if c2:
            if merged.head is not None:
                # Next of mc is ll2 head
                mc._next = c2
                # Move current of ll2 to its next
                c2 = c2._next
                # Move mc to its next
                mc = mc._next
                merged._size += 1
            else:
                merged.head = c2
                mc = merged.head
                c2 = c2._next
                merged._size += 1
    return merged
