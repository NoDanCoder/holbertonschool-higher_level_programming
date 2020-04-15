#!/usr/bin/python3
''' HTTP POST request with data '''

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    body = requests.post(url, data={'email': email})

    print(body.text)
