from datetime import datetime

def validate_task_title(title):
    if len(title) == 0 or len(title.strip()) == 0:
        raise ValueError("Title cannot be empty")
    return title


def validate_task_description(description):
    if len(description) == 0 or len(description.strip()) == 0:
        raise ValueError("Description cannot be empty")
    return description

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return due_date
    except ValueError:
        raise ValueError("Invalid date format")