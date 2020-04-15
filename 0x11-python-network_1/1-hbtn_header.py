#!/usr/bin/python3
''' Python script that get 'X-Request-Id' value from response head '''

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        body = response.info()

        print(body.get('X-Request-Id'))
