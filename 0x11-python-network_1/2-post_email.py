#!/usr/bin/python3
''' Python script that send a POST request with data '''

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body = response.read()

        print(body.decode('utf-8'))
