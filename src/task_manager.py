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

def list_tasks(status=None):
    tasks = load_tasks()  # Load all tasks

    if status:
        # Ensure the status is valid
        if status not in ["todo", "in-progress", "done"]:
            print(f"Error: Invalid status '{status}'. Valid statuses are 'todo', 'in-progress', and 'done'.")
            return

        # Filter tasks by the provided status
        filtered_tasks = [task for task in tasks if task["status"] == status]
    else:
        # If no status is provided, show all tasks
        filtered_tasks = tasks

    if not filtered_tasks:
        print("No tasks found.")
        return

    # Display tasks in a user-friendly format
    for task in filtered_tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']} (Created: {task['createdAt']})")


def mark_task(unique_id, new_status):
    tasks = load_tasks()

    # Find the task with the matching ID
    for task in tasks:
        if task["id"] == unique_id:
            task["status"] = new_status  # Update the status
            task["updatedAt"] = datetime.now().isoformat()  # Update the timestamp
            save_tasks(tasks)  # Save the updated tasks
            print(f"Task {unique_id} marked as {new_status}.")
            return
    # If no task with given ID is found
    print(f"Error: No task found with ID {unique_id}.")

def update_task(task_id, new_description):
    tasks = load_tasks()  # Load all tasks

    # Find the task with the matching ID
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description  # Update the description
            task["updatedAt"] = datetime.now().isoformat()  # Update the timestamp
            save_tasks(tasks)  # Save the updated tasks
            print(f"Task {task_id} updated successfully.")
            return

    # If no task with the given ID is found
    print(f"Error: No task found with ID {task_id}.")

def delete_task(task_id):
    tasks = load_tasks()  # Load all tasks

    # Filter out the task with the matching ID
    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(new_tasks) == len(tasks):
        print(f"Error: No task found with ID {task_id}.")
        return

    save_tasks(new_tasks)  # Save the updated list of tasks
    print(f"Task {task_id} deleted successfully.")
