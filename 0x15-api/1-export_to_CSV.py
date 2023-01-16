#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import json
import urllib.request
import csv

def get_todo_list(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    employee_name = ""
    for task in data:
        if employee_name == "":
            user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
            user_response = urllib.request.urlopen(user_url)
            user_data = json.loads(user_response.read())
            employee_name = user_data["name"]
    
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        
        for task in data:
            writer.writerow({'USER_ID': employee_id, 'USERNAME': employee_name,
                             'TASK_COMPLETED_STATUS': task["completed"], 'TASK_TITLE': task["title"]})
    print(f"Tasks data exported to {filename}.")

employee_id = input("Enter employee ID: ")
get_todo_list(int(employee_id))
