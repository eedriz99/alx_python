def safe_print_division(a, b):
        result = return( a / b)
    try:
        result
        
    except ZeroDivisionError:
        print("Inside result: None")
    finally:
        print("Inside result: {}".format(result))

safe_print_division(10, 0)