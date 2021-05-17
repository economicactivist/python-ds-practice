def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    split_phrase = phrase.split(" ")
    new_phrase_list = []
    for word in split_phrase:
        new_phrase_list.append(word.capitalize())
    
    return " ".join(new_phrase_list)
