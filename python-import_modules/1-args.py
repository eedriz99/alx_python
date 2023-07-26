def arguments(*args):
    if len(args) <= 1:
        print("{} argument:".format(len(args)))
    else:
        print("{} arguments:".format(len(args)))
    for arg in args:
        index = args.index(arg)
        print("{}: {}".format(index + 1, arg))
        # n = 0
        # while n < len(args):
        #     print("{}: {}".format(index + 1, arg))
        #     n += 1

arguments("hello")