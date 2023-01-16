#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """


import json
import urllib.request

def get_todo_list(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    employee_name = ""
    tasks = []
    for task in data:
        if employee_name == "":
            user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
            user_response = urllib.request.urlopen(user_url)
            user_data = json.loads(user_response.read())
            employee_name = user_data["name"]
        tasks.append({"task": task["title"], "completed": task["completed"], "username": employee_name})
    output = {str(employee_id): tasks}

    filename = f"{employee_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(output, json_file)
    print(f"Tasks data exported to {filename}.")

employee_id = input("Enter employee ID: ")
get_todo_list(int(employee_id))

