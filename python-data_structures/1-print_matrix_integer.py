def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for cell in row:
            if len(row) == 0:
                print(" ", end="\n")
            elif  row.index(cell) < len(row)-1:
                print("{:d}".format(cell), end=" ")
            else:
                print("{:d}".format(cell), end="\n")