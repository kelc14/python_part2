def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    count_close = parens.count(')')
    count_open = parens.count('(')
    for char in parens:
        if char == ')' and parens.index(char) == 0:
            return False
        if char == '(' and parens.index(char) == len(parens)-1:
            return False
        if count_close != count_open:
            return False
        else: return True

        
        return True
        
        