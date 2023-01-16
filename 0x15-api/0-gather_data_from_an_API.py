#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import json
import urllib.request

def get_todo_list(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    employee_name = ""
    completed_tasks = []
    total_tasks = len(data)
    for task in data:
        if task["completed"] == True:
            completed_tasks.append(task["title"])
        if employee_name == "":
            user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
            user_response = urllib.request.urlopen(user_url)
            user_data = json.loads(user_response.read())
            employee_name = user_data["name"]
    
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

employee_id = input("Enter employee ID: ")
get_todo_list(int(employee_id))
