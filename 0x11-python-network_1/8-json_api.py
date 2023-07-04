#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":
    # Set the letter as a parameter in the data dictionary
    data = {"q": argv[1] if len(argv) > 1 else ""}
    
    # Send a POST request to the specified URL with the letter as a parameter
    request = requests.post("http://0.0.0.0:5000/search_user", data=data)
    
    try:
        # Get the response as JSON
        json = request.json()
        
        if json:
            # Print the ID and name if a result is found
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            # Print "No result" if no result is found
            print("No result")
    except:
        # Print "Not a valid JSON" if an error occurs during JSON parsing
        print("Not a valid JSON")

