def left_join(ht1, ht2):
    """

    :param ht1: left hash table
    :param ht2: right hash table
    :return: list of joined values from both hash tables
    """
    results = []
    for item in ht1.table:
        while item is not None:
            key = item.val[0]
            joined = [key, ht1.get(key), ht2.get(key)]
            results.append(joined)
            item = item.next
    return results
