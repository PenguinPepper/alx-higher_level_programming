#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    the_last = number % 10
else:
    the_last = (abs(number) % 10) * -1

if (the_last > 5):
    print(f"Last digit of {number} is {the_last} and is greater than 5")
elif (the_last == 0):
    print(f"Last digit of {number} is {number % 10} and is 0")
elif (the_last < 6):
    print(f"Last digit of {number} is {the_last} and is less than 6 and not 0")
