#!/usr/bin/python3
"""sends a post request to the passed URL with the email as a parameter,
and finally displays the boody of the response
"""

import requests
import sys

if __name__ == "__main__":
    res = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(res.text)
