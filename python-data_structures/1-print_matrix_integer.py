def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for cell in row:
            if len(cell) == 0:
                print("{:d}".format(cell), end=" \n")
            elif  row.index(cell) < len(row)-1:
                print("{:d}".format(cell), end=" ")
            else:
                print("{:d}".format(cell), end="\n")
        # print("\n")

print_matrix_integer(matrix = [[]])