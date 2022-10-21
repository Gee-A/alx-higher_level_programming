#!/usr/bin/python3
"""fetch https://alx-intranet.hbtn.io/status using urllib
"""

import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as res:
        html = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- ut8 content: {}'.format(html.decode("utf-8", "replace")))

