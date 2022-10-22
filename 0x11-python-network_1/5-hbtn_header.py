#!/usr/bin/python3
"""sends a request to the URL and display the value of the variable
X-Request-Id in the response header."""

import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
