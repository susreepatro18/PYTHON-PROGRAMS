def determinant_2x2(matrix):
    """
    Calculate the determinant of a 2x2 square matrix.

    Parameters:
    - matrix: A 2x2 list representing the matrix [[a, b], [c, d]]

    Returns:
    - The determinant of the matrix (ad - bc)
    """
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Input matrix must be a 2x2 matrix")

    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]

    determinant = a * d - b * c
    return determinant

# Example usage
matrix = [[1, 2], [3, 4]]
print("Matrix:", matrix)
print("Determinant:", determinant_2x2(matrix))
