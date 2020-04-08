#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.
curl -sX OPTIONS -D - -o /dev/null "$1" | grep Allow: | cut -d' ' -f2-
