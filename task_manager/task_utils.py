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
def add_task(title, descrption, due_date):
    valid_title = validate_task_title(title)
    valid_desc = validate_task_description(descrption)
    valid_date = validate_due_date(due_date)

    
    if not valid_title[0] or not valid_desc[0] or not valid_date[0]:
        return

    tasks.append({
        "title": valid_title[1],
        "description": valid_desc[1],
        "due_date": valid_date[1],
        "completed": False
    })

    print("Task added successfully!")

#mark task as complete
def mark_task_as_complete(index, tasks=tasks):
        if index >= 0 and index < len(tasks):
            tasks[index]["completed"] = True
            print("Task marked as complete!")

# View pending tasks
def view_pending_tasks(tasks=tasks):
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

