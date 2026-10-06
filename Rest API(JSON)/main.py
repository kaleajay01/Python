from fastapi import FastAPI
import json

app = FastAPI()

def read_tasks():
    with open("tasks.json","r") as file:
        return json.load(file)
    

def write_tasks(tasks):
    with open("tasks.json","w") as file:
        json.dump(tasks, file, indent=4)
        
        
@app.get("/tasks")
def get_tasks():
    tasks = read_tasks()
    return tasks


@app.post("/tasks")
def create_task(task: dict):
    tasks = read_tasks()

    tasks.append(task)

    write_tasks(tasks)

    return {
        "message": "Task created successfully",
        "task": task
    }
    
    
# get one task
@app.get("/tasks/{task_id}")
def get_task(task_id:int):
    tasks = read_tasks()
    
    for task in tasks:
        if task["id"] == task_id:
            return task
        
        return{
            "message":"Task not found"
        }
        
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: dict):
    tasks = read_tasks()

    for task in tasks:
        if task["id"] == task_id:

            task["title"] = updated_task["title"]
            task["completed"] = updated_task["completed"]

            write_tasks(tasks)

            return {
                "message": "task updated successfully",
                "task": task
            }

    return {
        "message": "task not found"
    }

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = read_tasks()
    
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

            write_tasks(tasks)
            
            return{
                "message":"task deleted successfully"
            }
        
    return{
            "message"
        }