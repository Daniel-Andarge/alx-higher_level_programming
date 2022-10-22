#!/usr/bin/python3
"""
    Takes in a URL, sends a request to the URL and dsiplays
    value of the variable X-Request-Id
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print("{}".format(r.headers['X-Request-Id']))
