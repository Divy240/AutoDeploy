from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Task Model
class Task(BaseModel):
    text: str

# In-memory storage
tasks = []

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI 🚀"}

# Get all tasks
@app.get("/tasks")
def get_tasks():
    return tasks

# Add new task
@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task.text)
    return {"message": "Task added", "tasks": tasks}