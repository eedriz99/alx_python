#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

last_digit = str(number)[-1]

if int(last_digit) > 5:
    print("Last digit of {} is {} and is greater than 5 \n".format(number, last_digit))
elif int(last_digit) == 0:
    print("Last digit of {} is {} and is 0 \n".format(number, last_digit))
else:
    print("Last digit of {} is {} and is less than 6 and not 0 \n".format(number, last_digit))