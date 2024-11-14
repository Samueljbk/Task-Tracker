# Task Tracker CLI

A straightforward command-line interface (CLI) tool for efficiently tracking and managing your tasks. Built with Python, this lightweight task manager allows you to add, update, delete, and list tasks, while keeping track of their status: **todo**, **in-progress**, or **done**. All task data is saved in a simple `tasks.json` file, ensuring your tasks are persistently stored.

## About This Project

This project was built as a learning exercise and a portfolio piece to demonstrate my understanding of:
- Creating a command-line interface (CLI) application using **Python**.
- Handling user input and command-line arguments with **argparse**.
- Working with **JSON** for data persistence.
- Using Python's built-in modules for **file handling** and **data management**.
- Implementing features such as adding, updating, deleting, and filtering tasks efficiently.
- Following **best practices** for code organization, error handling, and user-friendly output.

The main goal was to build a functional and user-friendly CLI tool while gaining hands-on experience with core Python programming concepts and developing robust software engineering practices.

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
