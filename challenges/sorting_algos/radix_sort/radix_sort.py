def radix_sort(s):
    """Perform a radix sort on sequence.

    :param s: iterable sequence
    :return: new list of items from s in sorted order
    """
    if len(s) == 0:
        return s
    digit = 0
    max = s[0]
    max_digits = len(str(max))
    # Keep repeating until digit == the # of digits in the max value
    while digit <= max_digits:
        current_list = []
        # Loop over values to compare to current radix
        for i in range(10):
            for n in range(len(s)):
                max = s[n] if s[n] > max else max
                # Is the digit in s at index digit equal to i?
                # Logic suggested by: https://stackoverflow.com/a/42535516
                radix = s[n] // pow(10, digit) % 10
                if radix == i:
                    current_list.append(s[n])
            # We might not have to go all the way to 9 if our sorted_list is full
            if len(s) == len(current_list):
                break
        digit += 1
        s = current_list
        if 100 in s:
            print(s)
        # Only do this on the first pass
        if digit < 1:
            max_digits = len(str(max))
    return s