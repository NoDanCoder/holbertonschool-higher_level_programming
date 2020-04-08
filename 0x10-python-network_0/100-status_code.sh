#!/bin/bash
# Sends a request to a URL passed as an argument, and displays only the status code of the response.
curl "$1" -so /dev/null -w "%{http_code}"
