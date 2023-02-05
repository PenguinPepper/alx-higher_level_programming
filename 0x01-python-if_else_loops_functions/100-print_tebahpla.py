#!/usr/bin/python3
alpha = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - alpha)), end="")
    alpha = 32 if alpha == 0 else 0
