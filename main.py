from db.repository import TaskRepository
from service.task_service import TaskService

def main():
    db_params = "dbname=task_manager_db user=postgres password=YOUR_PASSWORD host=localhost"
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
                print(f"Success! Task '{new_task.title}' added with ID: {new_task.id}")
            except ValueError as e:
                print(f"Error! {e}")

        elif user_input == "2":

            try:
                tasks = service.show_tasks()
                if tasks == []:
                    print("No tasks found")
                
                for task in tasks:
                    print(f"[{task.id}] {task.title} - Status: {task.status}")
            except ValueError as e:
                print(f"Error! {e}")

        elif user_input == "3":
            
            try:
                id_input = input("Enter task ID to UPDATE: ")
                status_input = input(f"Enter a new status for task - id: {id_input}: ")

                service.update_task_status(id_input, status_input)
                print(f"Success! Task {id_input} status updated to '{status_input}'")
            except ValueError:
                print('Error! Invalid ID must be a number or validation failed!')

        elif user_input == "4":
            pass
        elif user_input == "5":
            print("Closing app...")
            break
        else:
            print("Invalid input! Try again!")

if __name__ == "__main__":
    main()