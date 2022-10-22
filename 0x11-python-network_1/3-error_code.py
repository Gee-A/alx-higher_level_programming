#!/usr/bin/python3
"""sends a request to the URL and display the body of the response
decoded in utf-8.
"""

import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8', "replace"))
    except urllib.request.HTTPError as e:
        print('Error code: {}'.format(e.code))
