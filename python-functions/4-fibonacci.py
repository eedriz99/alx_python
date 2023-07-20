def fibonacci_sequence(n):
    series = [0,1]
    if n > 1:
        x = 1
        while x < n-1:
            series.append(series[-1] + series[-2])
            x += 1
        return series
    elif n == 1:
        return [0]
    else:
        return []