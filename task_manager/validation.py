from datetime import datetime

def validate_task_title(title):
    title = title.strip()

    if len(title) < 3:
        return False, "Title too short"

    return True, title


def validate_task_description(description):
    description = description.strip()

    if len(description) < 5:
        return False, "Description too short"

    return True, description


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True, due_date
    except ValueError:
        return False, "Invalid date format"