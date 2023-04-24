#!/usr/bin/python3
"""
Script that fetches a URL
"""

if __name__ == "__main__":
    from urllib import request
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        restype = type(response.read())
        print(f"""Body response:
        -type: {restype}
        """)
