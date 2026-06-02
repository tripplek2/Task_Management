from datetime import datetime

# Import validation functions
from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Define tasks list
tasks = []

# Add task
def add_task(title, description, due_date):
    title = validate_task_title(title)
    description = validate_task_description(description)
    due_date = validate_due_date(due_date)

    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })

    print("Task added successfully!")

#mark task as complete
def mark_task_as_complete(index):
        if index < 0 or index >= len(tasks):
            raise ValueError("Invalid task index")
        
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    

# View pending tasks
def view_pending_tasks():
        pending = [t for t in tasks if not t["completed"]]

        if len(pending) == 0:
            print("No pending tasks")
            return

        for task in pending:
            print(task)

# Calculate progress
def calculate_progress(tasks=tasks):
        if len(tasks) == 0:
            return 0
        
        completed = len([t for t in tasks if t["completed"]])
        progress = (completed / len(tasks)) * 100
        return progress

