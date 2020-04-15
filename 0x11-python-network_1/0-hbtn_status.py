#!/usr/bin/python3
''' Python script that fetches a url '''

if __name__ == '__main__':
    import urllib.request

    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()

        display = {'type': type(body),
                   'content': body,
                   'utf8 content': body.decode('utf-8')}

        print('Body response:')

        for k, v in display.items():
            print('\t- {}: {}'.format(k, v))
