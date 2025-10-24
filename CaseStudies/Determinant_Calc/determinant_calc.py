def get_submatrix(matrix, row_to_remove, col_to_remove):
    """
    Creates a submatrix by removing a specified row and column.
    """
    return [
        [matrix[r][c] for c in range(len(matrix[0])) if c != col_to_remove]
        for r in range(len(matrix)) if r != row_to_remove
    ]

def calculate_determinant(matrix):
    """
    Calculates the determinant of a square matrix using cofactor expansion.
    """
    n = len(matrix)

    # Base case for 1x1 matrix
    if n == 1:
        return matrix[0][0]

    # Base case for 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for c in range(n):
        submatrix = get_submatrix(matrix, 0, c)
        cofactor = matrix[0][c] * calculate_determinant(submatrix)
        if c % 2 == 1:  # Apply alternating signs
            determinant -= cofactor
        else:
            determinant += cofactor
    return determinant

# Example Usage:
matrix_2x2 = [[1, 2], [3, 4]]
print(f"Determinant of 2x2 matrix: {calculate_determinant(matrix_2x2)}")

matrix_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Determinant of 3x3 matrix: {calculate_determinant(matrix_3x3)}")

matrix_4x4 = [[1, 0, 2, -1], [3, 0, 0, 5], [2, 1, 4, -3], [1, 0, 5, 0]]
print(f"Determinant of 4x4 matrix: {calculate_determinant(matrix_4x4)}")

