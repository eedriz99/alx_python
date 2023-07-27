def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for cell in row:
            if len(row) == 0:
                print("{:d} \n".format(cell))
            elif  row.index(cell) < len(row)-1:
                print("{:d}".format(cell), end=" ")
            else:
                print("{:d}".format(cell))
