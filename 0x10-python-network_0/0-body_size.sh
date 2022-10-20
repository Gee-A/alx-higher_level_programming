#!/bin/bash
# sends a request to the passed URL and display the size of the body
curl -s --head "$1" | grep 'Content-Length' | awk '{print $2}'
