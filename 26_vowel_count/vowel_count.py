def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    map = {}
    lower_phrase = phrase.lower();
    for char in 'aeiou':
        count = lower_phrase.count(char)
        if count>0:
            map[f'{char}'] = count
    return map