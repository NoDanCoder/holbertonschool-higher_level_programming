#!/usr/bin/python3
''' POST request and print the JSON response '''

if __name__ == '__main__':
    import requests
    from sys import argv

    argc = len(argv)

    url = 'http://0.0.0.0:5000/search_user'
    letter = argv[1] if argc > 1 else ""

    body = requests.post(url, data={'q': letter})

    try:
        doc = body.json()
        if doc == {}:
            print('No result')
        else:
            info = [doc.get('id'), doc.get('name')]
            print('[{}] {}'.format(*info))

    except ValueError:
        print('Not a valid JSON')
