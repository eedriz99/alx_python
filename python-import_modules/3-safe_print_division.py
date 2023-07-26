def safe_print_division(a, b):
    division = a / b
    return division
try:
    safe_print_division(a, b)
except ZeroDivisionError:
    print("Inside result: {}".format("None"))
finally:
    print("Inside result: {}".format(division))