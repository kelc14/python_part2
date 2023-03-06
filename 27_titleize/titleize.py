def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    word_list_original = phrase.split(' ')
    lower_words = []
    first_capital = []
    for word in word_list_original:
        lower_words.append(word.lower())
    for word in lower_words:
        first_capital.append(word.capitalize())
    return ' '.join(first_capital)