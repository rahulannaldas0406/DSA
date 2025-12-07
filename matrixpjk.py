A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

def add_matrices(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

print("Matrix A:")
print_matrix(A)
print("\nMatrix B:")
print_matrix(B)

print("\nSum of A and B:")
C = add_matrices(A, B)
print_matrix(C)
