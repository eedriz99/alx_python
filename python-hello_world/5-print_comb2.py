for num in range(100):
    if num != 99:
        print("{:0>2}".format(num), end=", ")
    else:
        print(num)