def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    new_list = []

    max_range = len(lst)    
    nums = range(max_range)

    for num in nums:
        if num%2 == 0:
            new_list.append(lst[num])
    return new_list

