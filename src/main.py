import argparse
from task_manager import add_task

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
    else:
        print("Unknown action")

if __name__ == "__main__":
    main()