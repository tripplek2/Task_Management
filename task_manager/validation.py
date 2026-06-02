from datetime import datetime

def validate_task_title(title):
    title = title.strip()

    if len(title) < 3:
        raise ValueError("Title too short")

    return title


def validate_task_description(description):
    description = description.strip()

    if len(description) < 5:
        raise ValueError("Description too short")

    return description


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return due_date
    except ValueError:
        raise ValueError("Invalid date format")