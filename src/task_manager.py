import json
from datetime import datetime
import os

# Load existing tasks from tasks.json
def load_tasks():
    if not os.path.exists('tasks.json'):
        return [] # Checking if tasks.json exists, returns nothing if it doesn't
    with open('tasks.json', 'r') as file:
        return json.load(file)

# Save new tasks to tasks.json
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Add new task to tasks.json
def add_task(description):
    tasks = load_tasks() # Current list of tasks

    # Creating a new task
    unique_id = len(tasks) + 1 
    new_task = {
        "id": unique_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Output: Task added successfully (ID: {unique_id})")