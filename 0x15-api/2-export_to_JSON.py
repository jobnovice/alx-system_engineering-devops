#!/usr/bin/python3
"""Export data to JSON format"""

import sys
import requests
import json

if len(sys.argv) < 2:
    print("Usage: python script.py <user_id>")
    exit(1)

user_id = int(sys.argv[1])

# Fetch user data
user_response = requests.get(f'https://jsonplaceholder' +
                             f'.typicode.com/users/{user_id}')
if user_response.status_code != 200:
    print("Failed to fetch user data.")
    exit(1)
user = user_response.json()

# Fetch todos data
todos_response = requests.get(f'https://jsonplaceholder' +
                              f'.typicode.com/todos?userId={user_id}')
if todos_response.status_code != 200:
    print("Failed to fetch todos data.")
    exit(1)
todos = todos_response.json()

# Construct data dictionary
data = {
    str(user_id): []
}

# Add todos to the tasks list
for todo in todos:
    task = {
        "task": todo["title"],
        "completed": todo["completed"],
        "username": user["username"]
    }
    data[str(user_id)].append(task)

# Export data to JSON file
filename = f'{user_id}.json'
with open(filename, 'w') as file:
    json.dump(data, file)
