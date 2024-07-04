#!/bin/bash
# Script that takes a URL, sends a request to the URL,
# and displaythe size of the body of the respoe
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
