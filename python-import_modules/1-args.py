def arguments(args):
    if len(args) == 1:
        print("{} argument:".format(len(args)))
    elif len(args) < 1:
        print("{} arguments.".format(len(args)))
    else:
        print("{} arguments:".format(len(args)))
    for arg in args:
        index = args.index(arg)
        print("{}: {}".format(index + 1, arg))

if __name__ == "__main__":
    import sys
    arguments(sys.argv[1:])