#!/usr/bin/python3
''' check status_code of HTTP GET request '''

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    body = requests.get(url)

    status = body.status_code
    if status >= 400:
        print('Error code: {}'.format(status))
    else:
        print(body.text)
