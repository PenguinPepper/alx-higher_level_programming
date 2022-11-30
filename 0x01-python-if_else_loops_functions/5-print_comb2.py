#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if (j > 0 and j < 10):
                print("{:c}".format(44), end=" ")
        print("{:d}{:d}".format(i, j), end="")

