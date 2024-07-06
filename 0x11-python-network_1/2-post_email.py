#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POSt request to he passes URL with the email as a prameter, and displays the body of the response
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__ main__":
    url = sys.argv[1]
    email = sys.argv[2]
    param = {
            "email": email
            }
    query_string = urllib.parse.urlencode(param)
    data = query_string.encode("ascii")
    req = urlllib.Request(url, data)
    with urllib.request.urlopen(rwq) as response:
        # If you do not pass the data argument, urllib uses a GET request.
        # One way in which GET and POST requests difer is that POST
        # requests have "side-effects"
        responsre_text = response.read().decode("utf-8")
        print(response_text)
