#!/usr/bin/python3
"""using API to get data and display it in a specific format"""

import requests
import sys

if len(sys.argv) != 2:
    print("Invalid input. Please provide the employee ID.")
    sys.exit(1)

try:
    employee_id = int(sys.argv[1])
except ValueError:
    print("Employee ID must be an integer.")
    sys.exit(1)

response = requests.get(
      f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
r2 = requests.get(
      f"https://jsonplaceholder.typicode.com/users/{employee_id}")
data = response.json()
d2 = r2.json()

completed_task = 0
for i in data:
    if i["completed"]:
        completed_task += 1

print(f"Employee {d2['name']}" +
      f"is done with tasks({completed_task}/{len(data)}):")

for i in data:
    if i["completed"]:
        print("\t ", i["title"])
