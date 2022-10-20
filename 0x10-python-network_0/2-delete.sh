#!/bin/bash
# sends a 'DELETE' request to the URL passed-in and displays the body of the response
curl -s "$1" -X DELETE
