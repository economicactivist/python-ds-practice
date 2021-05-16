def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    char_list = []

    for char in phrase:
        if char == to_swap.lower() or char == to_swap.upper():

            char_list.append(char.swapcase())
        else:
            char_list.append(char)
    return "".join(char_list)
