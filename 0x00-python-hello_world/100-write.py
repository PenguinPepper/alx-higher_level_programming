#!/usr/bin/python3
import sys
import subprocess
def print_to_stderror():
    sys.stderr.write('and that piece of art is useful - Dora Korpar, 2015-10-19\n')
    sys.exit(1)
print_to_stderror()
