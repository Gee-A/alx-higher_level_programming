#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of that response
curl -sI -o /dev/null -w '%{http_code}' "$1"
