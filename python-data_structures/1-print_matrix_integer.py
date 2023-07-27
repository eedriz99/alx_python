def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) <= 0:
            print("\n")
        else:
            for cell in row:
                if  row.index(cell) < len(row)-1:
                    print("{:d}".format(cell), end=" ")
                else:
                    print("{:d}".format(cell))
