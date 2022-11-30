#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 10):
        if (j < i or j == i):
            continue
        if (j > 0 and i < 8):
            print("{:d}{:d},".format(i, j), end=" ")
        else:
            print("{:d}{:d}".format(i, j))
