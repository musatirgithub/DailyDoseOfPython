def matrix_maker(x, y):
    matrix1 = (i*j for i in range(x) for j in range(y))
    return matrix1
matrix_maker(3, 5)
print(matrix1)
