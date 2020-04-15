#!/usr/bin/python3
''' GET a url and advice from HTTP failures '''

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]

    try:
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
    else:
        print(response.read().decode('utf-8'))
