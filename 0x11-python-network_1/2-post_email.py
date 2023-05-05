#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
"""


if __name__ == "__main__":
    from urllib import request, parse
    import sys

    url = sys.argv[1]
    values = {"email" : sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        res = response.read()
        print(res.decode('utf-8'))

