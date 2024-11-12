# Task Tracker CLI

A straightforward command-line interface (CLI) tool for efficiently tracking and managing your tasks. Built with Python, this lightweight task manager allows you to add, update, delete, and list tasks, while keeping track of their status: **todo**, **in-progress**, or **done**. All task data is saved in a simple `tasks.json` file, ensuring your tasks are persistently stored.

## Key Features
- **Add Tasks**: Quickly add new tasks with a description.
- **Update Tasks**: Modify existing task descriptions.
- **Delete Tasks**: Remove tasks you no longer need.
- **Mark Tasks**: Easily mark tasks as "in-progress" or "done".
- **List Tasks**: View all tasks or filter by status (todo, in-progress, done).
- **Search Tasks**: Find tasks by keywords in their descriptions.

## Example Usage
- **Add a Task**:
  ```bash
  python src/task_tracker.py add "Finish the project"

- **List all Tasks**:
  ```bash
  python src/task_tracker.py list "Finish the project"

- **Mark a Task as Done**:
  ```bash
  python src/task_tracker.py mark-done 1