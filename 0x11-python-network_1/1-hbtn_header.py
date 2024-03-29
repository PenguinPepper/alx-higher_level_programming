#!/usr/bin/python3
"""
Module contains script that takes in a URL sends a request and displays
the value of the X-Request-Id variable found in the header of the response
"""


if __name__ == "__main__":
    from urllib import request
    import sys

    with request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
