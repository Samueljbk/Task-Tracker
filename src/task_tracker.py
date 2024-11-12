import argparse
from task_manager import add_task, list_tasks, mark_task, update_task, delete_task

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    parser.add_argument(
        'action', 
        help="Action to perform: add, update, delete, list, mark-in-progress, mark-done"
        )
    parser.add_argument(
        'arguments', 
        nargs='*', help="Additional arguments for the action"
        )
    args = parser.parse_args()
    
    if args.action == "add":
        description = " ".join(args.arguments)
        add_task(description)
    elif args.action == "list":
        if args.arguments:
            status = args.arguments[0]
            list_tasks(status)
        else:
            list_tasks()
    elif args.action == "mark-in-progress":
        if args.arguments:
            unique_id = int(args.arugments[0])
            mark_task(unique_id, "in-progress")
        else:
            print("Error: Task ID is required to mark a task as in-progress.")
    elif args.action == "mark-done":
        if args.arguments:
            unique_id = int(args.arguments[0])
            mark_task(unique_id, "done")
        else:
            print("Error: Task ID is required to mark a task as done.")
    elif args.action == "update":
        if len(args.arguments) >= 2:
            unique_id = int(args.arguments[0])
            new_description = " ".join(args.arguments[1:])
            update_task(unique_id, new_description)
    elif args.action == "update":
        if len(args.arguments) >= 2:  # Ensure there are enough arguments
            task_id = int(args.arguments[0])  # Convert the first argument to an integer
            new_description = " ".join(args.arguments[1:])  # Join the rest as the new description
            update_task(task_id, new_description)
        else:
            print("Error: Task ID and new description are required to update a task.")
    elif args.action == "delete":
        if args.arguments:
            task_id = int(args.arguments[0])  # Convert the first argument to an integer
            delete_task(task_id)
        else:
            print("Error: Task ID is required to delete a task.")
    else:
        print("Unknown action")

if __name__ == "__main__":
    main()