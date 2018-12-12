from stack import Stack


def multi_bracket_validation(input_str):
    """Parse a string to determine if the grouping sequences within it are
    balanced.

    param: input_str (str) string to parse
    return: (boolean) True if input_str is balanced, else False
    """
    if type(input_str) is not str:
        raise TypeError('Input must be of type str')
    openers = ('[', '{', '(')
    opposites = {']': '[', '}': '{', ')': '('}
    stack = Stack()
    for c in input_str:
        # Push symbol if it's an opener
        if c in openers:
            stack.push(c)
        if c in opposites.keys():
            # If it's an opener, but its opposite isn't on the stack, return False
            if stack.pop().val != opposites[c]:
                return False
    # If we get here, and the top is None, all symbols found opposites
    if stack.top is None:
        return True
    return False
