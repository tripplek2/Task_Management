from datetime import datetime

def validate_task_title(title):
    if len(title.strip()) < 3:
        return False, "Title too short"
    return True, title.strip()


def validate_task_description(description):
    if len(description.strip()) < 5:
        return False, "Description too short"
    return True, description.strip()


def validate_due_date(due_date):
    try:
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d")
        return True, due_date
    except ValueError:
        return False, "Invalid date format"