def is_prime(number):
    div_list = []
    if number > 1:
        for n in range(1, number + 1):
            if number % n == 0:
                div_list.append(n)
        if len(div_list) == 2:
            return True
        else:
            return False
    else:
        return False