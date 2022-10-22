#!/usr/bin/python3

"""takes my GitHub credentials (username and password) and uses the GitHub API
to display your id
"""

import sys
import requests

if __name__ == "__main__":
    res = requests.get('https://api.github.com/user',
                       auth=(sys.argv[1], sys.argv[2]))
    if res.status_code >= 400:
        print('None')
    else:
        print(res.json().get('id'))
