import json
from datetime import datetime
import os

# Load existing tasks from tasks.json
def load_tasks():
    if not os.path.exists('tasks.json'):
        return [] # Checking if tasks.json exists, returns nothing if it doesn't
    with open('tasks.json', 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)