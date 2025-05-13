import csv
from models import Task, TaskWithID

DATABASE_FILENAME = 'tasks.csv'

column_fields = ["id", "title", "description", "status"]

def read_all_tasks() -> list[TaskWithID]:
    with open(DATABASE_FILENAME) as csvfile:
        reader = csv.DictReader(csvfile)
        return [TaskWithID(**row) for row in reader]
    
def read_task(task_id) -> TaskWithID | None:
    with open(DATABASE_FILENAME) as csvfile:
        reader = csv.DictReader(csvfile)
    for row in reader:
        if int(row["id"]) == task_id:
            return TaskWithID(**row)
        
def get_next_id():
    try:  
        with open(DATABASE_FILENAME, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            max_id = max(int(row["id"] for row in reader))
            return max_id + 1
    except (FileNotFoundError, ValueError):
        return 1
    
def write_task_into_csv(task: TaskWithID):
    with open(DATABASE_FILENAME, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=column_fields)
        writer.writerow(task.model_dump())
        
def create_task(task: Task) -> TaskWithID:
    id = get_next_id()
    task_with_id = TaskWithID(id=id, **task.model_dump())
    write_task_into_csv(task_with_id)
    return task_with_id

def modify_task(id: int, task: dict) -> TaskWithID | None:
    updated_task: TaskWithID | None = None
    tasks = read_all_tasks()
    for number, task_ in enumerate(tasks):
        if task_.id == id:
            tasks[number] 

    
    with open(DATABASE_FILENAME, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_fields)
        writer.writeheader()
        for task in tasks:
            writer.writerow(task.model_dump())
        if updated_task:
            return updated_task
        
def remove_task(id: int) -> TaskWithID | None:
    deleted_task: Task | None 
    tasks = read_all_tasks()
    with open(DATABASE_FILENAME, mode = "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_fields)
        writer.writeheader()
        for task in tasks:
            if task.id == id:
                deleted_task = task
                continue
            writer.writerow(task.model_dump())
            
        if deleted_task:
            return deleted_task