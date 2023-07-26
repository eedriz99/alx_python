def safe_print_division(a, b):
    
    try:
        result = a / b
        # return result
    except ZeroDivisionError:
        result = None
        # print("Inside result: {}")
    finally:
        print("Inside result: {}".format(result))

safe_print_division(10, 0)