from datetime import datetime

# Import validation functions
from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    try:
        title = validate_task_title(title)
        description = validate_task_description(description)
        due_date = validate_due_date(due_date)
    except ValueError as e:
        print(e)
        return

    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })

    print("Task added successfully!")


# Implement mark_task_as_complete function
def mark_task_as_complete(index):
    index -= 1
    if index < 0 or index >= len(tasks):
        print("Invalid task index")
        return

    tasks[index]["completed"] = True
    print("Task marked as complete!")


# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]

    if len(pending) == 0:
        print("No pending tasks")
        return

    for task in pending:
        print(task)


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0

    completed = len([t for t in tasks if t["completed"]])
    progress = (completed / len(tasks)) * 100
    return progress
