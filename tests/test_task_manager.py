import unittest
import json
import os
from datetime import datetime
from task_manager import add_task, list_tasks, mark_task, update_task, delete_task

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # Create a test tasks file
        self.test_file = 'test_tasks.json'
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def tearDown(self):
        # Clean up test file after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_add_task(self):
        add_task("Test task")
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['description'], "Test task")
        self.assertEqual(tasks[0]['status'], "todo")
    
    def test_mark_task(self):
        add_task("Test task")
        mark_task(1, "in-progress")
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        self.assertEqual(tasks[0]['status'], "in-progress")
    
    def test_update_task(self):
        add_task("Original task")
        update_task(1, "Updated task")
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        self.assertEqual(tasks[0]['description'], "Updated task")
    
    def test_delete_task(self):
        add_task("Test task")
        delete_task(1)
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        self.assertEqual(len(tasks), 0)

if __name__ == '__main__':
    unittest.main()