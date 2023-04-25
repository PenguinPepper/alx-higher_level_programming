#!/usr/bin/python3
"""
Script that fetches a URL
"""

if __name__ == "__main__":
    from urllib import request
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        cod = response.peek()
        # vy = response.url()
        restype = type(response.read())
        print(f"""Body response:""")
        print(f"    -type: {restype}")
        print(f"    -content: {cod}")
        if response.headers.get_content_charset() == 'utf-8':
            print(f"    -utf-8 content: OK")
