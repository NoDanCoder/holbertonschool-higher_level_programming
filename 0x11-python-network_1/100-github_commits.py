#!/usr/bin/python3
''' Get 10 lastest commits of a given repo and user (Github API) '''

if __name__ == "__main__":
    import requests
    from sys import argv

    repo = argv[1]
    user = argv[2]
    url = 'https://api.github.com/'

    body = requests.get(url + 'repos/' + user + '/' + repo + '/commits')
    commits = body.json()

    for i in commits[:10]:
        sha = i.get('sha')
        author = i.get('commit').get('author').get('name')

        print('{}: {}'.format(sha, author))
