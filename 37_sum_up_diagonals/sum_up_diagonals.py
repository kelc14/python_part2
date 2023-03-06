def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    tl_to_br_index = 0
    bl_to_tr_index = len(matrix) - 1
    sum = 0
    for row in matrix:
        sum += row[tl_to_br_index]
        sum += row[bl_to_tr_index]
        bl_to_tr_index -= 1
        tl_to_br_index +=1
    print(sum)
