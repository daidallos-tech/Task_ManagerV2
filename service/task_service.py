from db.repository import TaskRepository
from models.task import Task

class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def add_task(self, title, description):
        if not title.strip():
            raise ValueError("Your title cannot be empty!")
        
        if len(title.strip()) > 50:
            raise ValueError("Your title cannot contain more than 50 symbols!")
        
        task = Task(title, description)
        return self.repository.create_task(task)
    
    def show_tasks(self):
        return self.repository.get_all_tasks()
    
    def update_task_status(self, id, status):
        pass