def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for cell in row:

            if  row.index(cell) < len(row)-1:
                print("{:d}".format(cell), end=" ")
            else:
                print("{:d}".format(cell),)
        print("\n")