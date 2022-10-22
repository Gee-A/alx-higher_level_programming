#!/usr/bin/python3
"""takes a letter and sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter
"""

import sys
import requests

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 and \
                    not isinstance(sys.argv[1], int) else ""
    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    dic = res.json()
    if dic == {}:
        print('No result')
    else:
        print('[{}] {}'.format(dic.get('id'), dic.get('name')))
