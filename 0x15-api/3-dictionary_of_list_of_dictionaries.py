#!/usr/bin/python3
""""Exporting all emplyees data to JSON format with a specfic format"""

import json
import requests

filename = 'todo_all_employees.json'

users = requests.get('https://jsonplaceholder.typicode.com/users').json()

data1 = {}

for user in users:
    data = {
        str(user['id']): []
    }
    todos = requests.get(f'https://jsonplaceholder.typicode.com/users/' +
                         f'{str(user["id"])}/todos').json()
    for task in todos:
        task = {
            "task": task["title"],
            "completed": task["completed"],
            "username": user["username"]
        }
        data[str(user['id'])].append(task)
    data1.update(data)

with open(filename, 'w') as file:
    json.dump(data1, file)
