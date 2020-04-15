#!/usr/bin/python3
''' HTTP GET request and print X-Request-Id property from response head '''

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    body = requests.get(url)

    print(body.headers['X-Request-Id'])
