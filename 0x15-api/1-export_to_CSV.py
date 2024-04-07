#!/usr/bin/python3
"""using what we did earlier we now have to export the data to csv format"""
import csv
import requests
import sys

if (len(sys.argv) < 2):
    print("gotta provide the id")
    exit(1)
user_id = int(sys.argv[1])

users_list = requests.get(
    f'https://jsonplaceholder.typicode.com/users/{user_id}')
users = users_list.json()
todos_list = requests.get(
    f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
todos = todos_list.json()
# define the fields
fields = ["userId", "username", "completed", "title"]

csv_file = f"{user_id}.csv"

with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields, quoting=csv.QUOTE_ALL)
    # writer.writeheader()
    for todo in todos:
        modified_todo = {
            'userId': f'{todo["userId"]}',
            'username': f'{users["username"]}',
            'completed': f'{todo["completed"]}',
            'title': f'{todo["title"]}'
        }
        writer.writerow(modified_todo)
