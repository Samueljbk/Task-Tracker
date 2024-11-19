# Task Tracker CLI

A straightforward command-line interface (CLI) tool for efficiently tracking and managing your tasks. Built with Python, this lightweight task manager allows you to add, update, delete, and list tasks, while keeping track of their status: **todo**, **in-progress**, or **done**.

## Features
- ✨ Add, update, and delete tasks
- 📋 List all tasks or filter by status
- 🔄 Track task status (todo, in-progress, done)
- 📅 Automatic timestamp tracking
- 💾 Persistent storage using JSON
- 🔍 Search functionality
- ⚡ Fast and lightweight

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/task-tracker-cli.git
cd task-tracker-cli
```

2. Install dependencies:
```bash
pip install -e .
```

## Usage

### Adding Tasks
```bash
task-manager add "Complete project documentation"
```

### Listing Tasks
```bash
# List all tasks
task-manager list

# List tasks by status
task-manager list todo
task-manager list in-progress
task-manager list done
```

### Updating Tasks
```bash
# Update task description (replace 1 with your task ID)
task-manager update 1 "Updated task description"

# Mark task as in-progress
task-manager mark-in-progress 1

# Mark task as done
task-manager mark-done 1
```

### Deleting Tasks
```bash
task-manager delete 1
```

## Project Structure
```
task-manager/
├── src/
│   ├── __init__.py
│   ├── task_manager.py    # Core functionality
│   └── task_tracker.py    # CLI interface
├── tests/
│   ├── __init__.py
│   └── test_task_manager.py
├── data/
│   └── tasks.json
├── README.md
├── requirements.txt
└── setup.py
```

## Technical Details

### Built With
- Python 3.6+
- argparse - For CLI argument parsing
- json - For data persistence
- datetime - For timestamp tracking
- unittest - For testing

### Data Storage
Tasks are stored in a JSON file with the following structure:
```json
{
    "id": 1,
    "description": "Task description",
    "status": "todo",
    "createdAt": "2024-11-19T10:00:00",
    "updatedAt": "2024-11-19T10:00:00"
}
```

## Development

### Running Tests
```bash
pytest tests/
```

### Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Enhancements
- [ ] Due dates for tasks
- [ ] Priority levels
- [ ] Task categories/tags
- [ ] Export tasks to different formats (CSV, HTML)
- [ ] Database integration
- [ ] Task completion statistics

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments
- Inspired by various task management tools
- Built as a learning project to demonstrate Python CLI development