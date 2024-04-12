#!/usr/bin/python3
"""using what we did earlier we now have to export the data to json format"""

import sys
import requests
import json

if (len(sys.argv) < 2):
    print("gotta provide more arguments")
    exit(1)
user_id = int(sys.argv[1])



user =  requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}').json()
todos = requests.get(f'https://jsonplaceholder.typicode.com/todos?{user_id}').json()

# data = {
#     for todo in todos:
#         "tasks":   
# }

filename = f'{user_id}.json'

with open(filename, 'w') as file:
    json.dump(f'{user_id}:' + 
                [{"task": todos["title"],
                  "completed": todos["completed"],
                  "username": user["username"]}], filename, indent=2)