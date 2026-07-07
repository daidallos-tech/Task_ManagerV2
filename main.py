from db.repository import TaskRepository
from service.task_service import TaskService
from db.database import init_db
from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")

    db_params = (f"dbname={db_name} user={db_user} password={db_pass} host={db_host}")

    init_db(db_params)

    repository = TaskRepository(db_params)
    service = TaskService(repository)

    while True:
        print("=== TASK MANAGER ===")
        print("1 - to ADD task")
        print("2 - to SHOW tasks")
        print("3 - to UPDATE task")
        print("4 - to DELETE task")
        print("5 - to EXIT")

        user_input = input("Enter your choice: ")

        if user_input == "1":
            
            title_input = input("Enter a title of your task: ")
            description_input = input("Enter a description of your task: ")

            try:
                new_task = service.add_task(title_input, description_input)
                print(f"\nSuccess! Task '{new_task.title}' added with ID: {new_task.id}\n")
            except ValueError as e:
                print(f"Error! {e}")

        elif user_input == "2":

            try:
                tasks = service.show_tasks()
                if tasks == []:
                    print("No tasks found")
                
                print("")
                print("   === TASKS ===")
                print("")
                for task in tasks:
                    print(f"[{task.id}] {task.title} - Status: {task.status}")
                print("")
            except ValueError as e:
                print(f"Error! {e}")

        elif user_input == "3":
            
            try:
                id_input = int(input("Enter task ID to UPDATE: "))
                status_input = input(f"Enter a new status for task - id: {id_input}: \n")

                service.update_task_status(id_input, status_input) # type: ignore
                print(f"Success! Task '{task.title}' status updated to '{status_input}'\n")
            except ValueError:
                print('Error! Invalid ID must be a number or validation failed!')

        elif user_input == "4":
            
            try:
                id_input = int(input("Enter task ID to DELETE: "))

                service.delete_task_id(id_input)
                print(f"\nSuccess! Task '{task.title}' was deleted from your list!\n")
            except ValueError:
                print("Error! Invalid ID must be a number or validation failed!")

        elif user_input == "5":
            print("Closing app...")
            break
        else:
            print("Invalid input! Try again!")

if __name__ == "__main__":
    main()