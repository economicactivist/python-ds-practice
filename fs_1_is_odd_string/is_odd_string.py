def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    word = word.lower()
    num_list = list(range(1, 27))
    split_alphabet = list("abcdefghijklmnopqrstuvwxyz")

    zipped_alphabet_dict = dict(list(zip(split_alphabet, num_list)))

    count =  0
    for letter in word:
        count += zipped_alphabet_dict[letter]

    return True if count%2==1 else False


    # Hint: you may find the ord() function useful here
