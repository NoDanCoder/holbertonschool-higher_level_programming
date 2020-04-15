#!/usr/bin/python3
'''  Python script that fetches a URL using the requests package '''

if __name__ == '__main__':
    import requests

    url = 'https://intranet.hbtn.io/status'
    body = requests.get(url).text

    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format(body))
