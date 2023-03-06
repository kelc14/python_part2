def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    list = []
    for letter in phrase:
        if (to_swap.isupper()):
            list.append(letter.swapcase()) if letter.upper() == to_swap else list.append(letter)
        else:
            list.append(letter.swapcase()) if letter.lower() == to_swap else list.append(letter)
        
    return ''.join(list)