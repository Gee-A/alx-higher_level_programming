#!/bin/bash
# sends a 'GET' request to the passed-in URL, and displays the body of the response
curl -s "$1" -X GET -L
