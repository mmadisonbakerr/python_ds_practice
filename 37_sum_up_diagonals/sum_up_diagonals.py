def sum_up_diagonals(matrix):
    total = 0

    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-1 - i]

    return total

    # return sum(matrix[i][len(matrix)-i-1] for i in range(len(matrix)))


    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:"""

m1 = [
    [1,   2],
    [30, 40],
]
print(sum_up_diagonals(m1))
        # 73

m2 = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9],
]
print(sum_up_diagonals(m2))
        # 30
