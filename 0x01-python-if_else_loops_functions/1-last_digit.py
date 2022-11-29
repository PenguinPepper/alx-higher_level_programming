#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if ((number % 10) > 5):
    print(f"Last digit of {number} is {number % 10} and is greater than five")
elif ((number % 10) == 0):
    print(f"Last digit of {number} is {number % 10} and is zero")
elif ((number + (number // 10) * 10) < 6):
    print(f"Last digit of {number} is {number + (number // 10) * 10} and is less than six and not zero")
