def binary_search(search_list, search_key):
    left_idx, right_idx = 0, len(search_list) - 1
    # while True:
    for _ in range(10):
        if right_idx - left_idx < 1:
            return -1
        mid_idx = (right_idx - left_idx) // 2
        # search_key is at mid_idx
        if search_key == search_list[mid_idx]:
            return mid_idx
        # search_key is left of mid_idx
        if search_key < search_list[mid_idx]:
            right_idx = mid_idx
        elif search_key > search_list[mid_idx]:
            left_idx = mid_idx
        # Subrange is empty

        print('search_key=', search_key, 'left_idx=', left_idx, 'mid_idx=', mid_idx,
              'search_list[mid_idx]=', search_list[mid_idx], 'right_idx=', right_idx)


if __name__ == '__main__':
    pass
