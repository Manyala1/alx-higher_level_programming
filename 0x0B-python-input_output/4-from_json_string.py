#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a string-to-JSON function"""
import json

def from_json_string(my_str):
        """Return the python object representation of a JSON string"""
        return json.loads(my_str)
