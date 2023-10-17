#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
value = number % 10

if number > 0:
    if value > 5:
        print(f"Last digit of {number:d} is {value:d} and is greater than 5")
    elif value < 6 and value != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, value))
    else:
        print(f"Last digit of {number:d} is {value:d} and is 0")
elif number == -1:
    neg = number

    print(f"Last digit of {number:d} is {neg:d} and is less than 6 and not 0")
else:
    new = number * -1
    new = new % 10
    num = new * -1

    if new == 0:
        print(f"Last digit of {number:d} is {new:d} and is 0")
    else:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, num))
