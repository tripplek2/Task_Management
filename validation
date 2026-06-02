from datetime import datetime

def validate_task_title(title):
    if len(title.strip()) < 3:
        raise ValueError("Title too short")
    return title.strip()


def validate_task_description(description):
    if len(description.strip()) < 5:
        raise ValueError("Description too short")
    return description.strip()


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return due_date
    except ValueError:
        raise ValueError("Invalid date format")