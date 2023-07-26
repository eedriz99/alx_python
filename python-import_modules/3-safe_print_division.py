def safe_print_division(a, b):
        result = a / b
    try:
        return result
    except ZeroDivisionError:
        print("Inside result: None")
    finally:
        print("Inside result: {}".format(result))
