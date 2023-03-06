def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.
    
    oldest = 0
    second_oldest = 0
    for age in ages:
        print(isinstance(age,int))
        
        if age >= oldest:
            second_oldest = oldest if age != oldest else second_oldest
            oldest = age
            print(oldest, 'oldest')
        elif age >= second_oldest:
            second_oldest = age
            print(second_oldest, 'second')
    return (second_oldest, oldest)
