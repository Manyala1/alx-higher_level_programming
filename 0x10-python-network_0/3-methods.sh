#!/bin/bash
# Script that takes a URL and dsisplays all HTTP methods the server will accept
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
