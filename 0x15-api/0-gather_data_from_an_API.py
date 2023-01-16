#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
import sys


 url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos'
    req = requests.get(url)
    com_tasks = []
    no = 0
    for task in req.json():
        if task.get('completed'):
            com_tasks.append(task.get('title'))
        no += 1
    url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
    req = requests.get(url)
    name = req.json().get('name')
    msg = f'Employee {name} is done with tasks({len(com_tasks)}/{no}:'
    print(msg)
    for task in com_tasks:
        print('\t ' + task)
