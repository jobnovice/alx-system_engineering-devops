#!/usr/bin/python3
"""using API to get data and display it in a specific format"""

import requests
import sys

if (len(sys.argv) == 2):
	if type(sys.argv[1]) != int and sys.argv[1] > 11 and sys.argv[1] < 0:
		print("Not a valid number")
		exit()
else:
	print("invalid input need to give us the employee ID")
	exit()	

response = requests.get("https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos")
r2 = requests.get("https://jsonplaceholder.typicode.com/users/{sys.argv[1]}")
data = response.json()
d2 = r2.json()

print("Employee {d2.get('name')} is done with tasks({len(data.get('completed'))}/{len(data)})")


