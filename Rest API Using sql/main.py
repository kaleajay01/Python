from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/taskdb"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255),nullable=False)
    completed = Column(Boolean, default=False)
    

#display all code
@app.get("/tasks")
def get_tasks():
    
    db = SessionLocal()
    
    tasks = db.query(Task).all()
    
    db.close()
    
    return tasks

#display the task by id
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    
    db = SessionLocal()
    
    task = db.query(Task).filter(Task.id == task_id).first()
    
    db.close()
    
    if task is None:
        return{
            "message":"task not found"
        }
    
    return task


#insert data in database
#add new task
@app.post("/tasks")
def create_task(task: dict):
    
    db = SessionLocal()
    
    new_task = Task(
        title = task["title"],
        completed = task["completed"]
    )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    db.close()
    
    return{
        "message":"task create successfully",
        "task":new_task
    }
    
#update the data
#delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id, int):
    
    db = SessionLocal()
    
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if task is None:
        db.close()
        
        return{
            "message":"task not found"
        }
        
    db.delete(task)
    db.commit()
    
    db.close()
    
    return{
        "message":"task deleted successfully"
    }
    
#update the task
@app.put("/tasks/{task_id}")
def update_task(task_id:int, updated_task: dict):
    
    db = SessionLocal()
    
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if task is None:
        db.close()
        
        return{
            "message":"task not found"
        }
        
    task.title = updated_task["title"]
    task.completed = updated_task["completed"]
    
    db.commit()
    db.refresh(task)
    
    db.close()
    
    return{
        "message":"task updated successfully",
        "task":task
    }