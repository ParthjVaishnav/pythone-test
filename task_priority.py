from datetime import datetime

def task_manager(tasks, current_date):
    result = {
        "Overdue Tasks": [],
        "Priority Breakdown": {
            "Low": [],
            "Medium": [],
            "High": []
        }
    }

    # Convert current date to datetime
    current = datetime.strptime(current_date, "%Y-%m-%d")

    for task in tasks:
        # Check overdue
        deadline = datetime.strptime(task["deadline"], "%Y-%m-%d")
        if deadline < current:
            result["Overdue Tasks"].append(task["task_name"])

        # Priority categorization
        if task["priority"] == 1:
            result["Priority Breakdown"]["Low"].append(task["task_name"])
        elif task["priority"] == 2:
            result["Priority Breakdown"]["Medium"].append(task["task_name"])
        elif task["priority"] == 3:
            result["Priority Breakdown"]["High"].append(task["task_name"])

    return result


# Example input
tasks = [
    {"task_id": 1, "task_name": "Write Report", "deadline": "2025-07-10", "priority": 2},
    {"task_id": 2, "task_name": "Code Review", "deadline": "2025-07-12", "priority": 3},
    {"task_id": 3, "task_name": "Update Database", "deadline": "2025-07-16", "priority": 1},
    {"task_id": 4, "task_name": "Test API", "deadline": "2025-07-14", "priority": 2}
]

current_date = "2025-07-15"

print(task_manager(tasks, current_date))
