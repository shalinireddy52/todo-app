tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def view_tasks():
    for idx, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Incomplete"
        print(f"{idx + 1}. {task['task']} [{status}]")

def mark_task_completed(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
