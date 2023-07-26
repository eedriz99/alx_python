def raise_exception_msg(message=""):
    try:
        raise NameError('{}'.format(message))