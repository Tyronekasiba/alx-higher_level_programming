#!/usr/bin/python3
"""A python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code"""

from urllib import request, error
from sys import argv

if __name__ == "__main__":
        try:
            with request.urlopen(argv[1]) as page:
                print(page.read().decode('utf-8'))
        except error.HTTPError as e:
            print("Error code: {}".format(e.code))
