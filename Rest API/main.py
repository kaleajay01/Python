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
    
    