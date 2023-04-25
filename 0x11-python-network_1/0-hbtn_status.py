#!/usr/bin/python3
"""
Script that fetches a URL
"""

if __name__ == "__main__":
    from urllib import request
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        cod = response.read()
        # vy = response.url()
        restype = type(cod)
        print(f"""Body response:""")
        print(f"    - type: {restype}")
        print(f"    - content: {cod}")
        print(f"    - utf-8 content: {cod.decode('utf-8')}")
