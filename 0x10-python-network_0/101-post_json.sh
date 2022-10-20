#!/bin/bash
# sends a JSON POST resquest to a URL passed as the first argument, and displays the body of the reponse
curl -s -x POST "$1" -H "Content-Type: application/json" -d @"$2"
