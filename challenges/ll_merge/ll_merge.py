from .linked_list import LinkedList
from .node import Node


def ll_merge(ll1, ll2):
    print('ll1', ll1)
    print('ll2', ll2)
    merged = LinkedList()
    merged.head = ll1.head
    merged._size = ll1._size
    cur_merged = ll1.head
    ll1.head = ll1.head._next
    cur_merged._next = ll2.head
    ll2.head = ll2.head._next
    cur_merged = cur_merged._next
    while ll1.head._next or ll2.head._next:
        cur_merged._next = ll1.head

        ll1.head = ll1.head._next
        cur_merged = cur_merged._next
        cur_merged._next = ll2.head
        ll2.head = ll2.head._next
        cur_merged = cur_merged._next

        print('ll1', ll1)
        print('ll2', ll2)
        print('merged =', merged)

    print(merged)
    return merged

