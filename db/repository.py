import psycopg2
from models.task import Task

class TaskRepository:
    def __init__(self, db_params: str):
        self.db_params = db_params
    
    # CREATE
    def create_task(self, task: Task) -> Task:
        conn = psycopg2.connect(self.db_params)

        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO tasks(title, description, status)
                    VALUES (%s, %s, %s) 
                    RETURNING id;
                """, (task.title, task.description, task.status))

                generated_id = cur.fetchone()[0] # type: ignore

                task.id = generated_id

        conn.close()
        return task

    # READ
    def get_all_tasks(self) -> list[Task]:
        conn = psycopg2.connect(self.db_params)

        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT id, title, description, status FROM tasks
                """)

                tasks = cur.fetchall()

                tasks_lst = []

                for task in tasks:
                    filter_task = Task(task[1], task[2], task[3], task[0])
                    tasks_lst.append(filter_task)
        
        conn.close()
        return tasks_lst

    def get_task_by_id(self, id):
        conn = psycopg2.connect(self.db_params)

        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT title, description, status, id FROM tasks WHERE id = %s;
                """, (id,))

                row = cur.fetchone()

                if row is None:
                    conn.close()
                    return None
        
                task = Task(title=row[0], description=row[1], status=row[2], id=row[3])
                
        conn.close()
        return task
    
    def update_task(self, task: Task):
        conn = psycopg2.connect(self.db_params)

        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE tasks SET status = %s WHERE id = %s;
                """, (task.status, task.id))
        
        conn.close()
    
    def delete_task(self, id: int):
        conn = psycopg2.connect(self.db_params)

        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM tasks WHERE id = %s;
                """, (id,))
        
        conn.close()

    