#!/usr/bin/python3
''' Uses Github API to get id of user [user:token] '''

if __name__ == '__main__':
    import requests
    from sys import argv

    user = argv[1]
    pwd = argv[2]

    url = 'https://api.github.com/user'
    body = requests.get(url, auth=(user, pwd))

    print(body.json().get('id'))
