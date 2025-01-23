from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import json 
from typing import Dict

app = FastAPI()

# Mount the static files for the frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

class Task(BaseModel):
    title: str
    due_date: str

def load_tasks() -> Dict:
    try:
        with open('app/tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_tasks(tasks: Dict):
    with open('app/tasks.json', 'w') as file:
        json.dump(tasks, file)

@app.get("/")
async def serve_ui():
    return FileResponse("static/index.html")

@app.get("/tasks")
async def get_tasks():
    tasks = load_tasks()
    return tasks

@app.post("/tasks")
async def add_task(task: Task):
    tasks = load_tasks()
    task_id = str(len(tasks) + 1)
    tasks[task_id] = task.dict()
    save_tasks(tasks)
    return {"message": "Task added successfully!"}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    tasks = load_tasks()
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    save_tasks(tasks)
    return {"message": "Task deleted successfully!"}