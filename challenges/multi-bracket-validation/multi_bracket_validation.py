from stack import Stack

def multi_bracket_validation(input_str):
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
            if stack.peek().val != opposites[c]:
                return False
            # Pop the symbol if c is its opposite and keep going
            stack.pop()
    # If we get here, and the top is None, all symbols found opposites
    if stack.top is None:
        return True
    return False

