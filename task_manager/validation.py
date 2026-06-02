from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str):
        return False, "Title must be a string"
    
    if len(title.strip()) < 3:
        return False, "Title must be atleast 3 characters"
    
    return True, title.strip()

def validate_task_description(description):
    if not isinstance(description, str):
        return False, "Description must be a string"

    if len(description.strip()) < 5:
        return False, "Description must be at least 5 characters"

    return True, description.strip() 

def validate_due_date(due_date):
    try:
        datetime.striptime(due_date,"%Y-%m-%d")
        return True, due_date
    except ValueError:
        return False, "Date must be YYYY-MM-DD"