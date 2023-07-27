def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for cell in row:
            if  row.index(cell) < len(row)-1:
                print("{}".format(cell), end=" ")
            else:
                print("{}".format(cell), end="\n")
        # print("\n")

print_matrix_integer(matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])