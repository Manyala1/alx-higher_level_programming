#!/usr/bin/python3
import urllib.request
import sys
"Get the url from the command line arguments"
url = sys.argv[1]
" Fetch the urllib and print the value of the X-Request-Id header"
with urllib.request.urlopen(url) as response:
    x_request_id = response.getheader('X-Request-Id')
    print(x_request_id)
