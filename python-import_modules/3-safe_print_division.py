def safe_print_division(a, b):
    try:
        division = a / b
    except ZeroDivisionError:
        print("Inside result: {}".format("None"))
    finally:
        print("Inside result: {}".format(division))