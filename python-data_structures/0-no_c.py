def no_c(my_string):
    l = []
    for string in my_string:
        if string.upper() == 'C':
            continue
        else:
            l.append(string)
    new_string = "".join(l)
    return new_string