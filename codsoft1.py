tasks = []
def display_tasks():
    if not tasks:
        print("\nNo tasks in your to-do list!")
        return
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['name']} - {task.get('description', 'No description')}")
def add_task():
    name = input("\nEnter task name: ")
    description = input("Enter task description (optional): ")
    tasks.append({"name": name, "description": description, "completed": False})
    print("Task added successfully!")
def toggle_task_status():
    display_tasks()
    try:
        task_number = int(input("\nEnter the task number to toggle status: ")) - 1
        tasks[task_number]["completed"] = not tasks[task_number]["completed"]
        print("Task status updated!")
    except (IndexError, ValueError):
        print("Invalid task number!")
def edit_task():
    display_tasks()
    try:
        task_number = int(input("\nEnter the task number to edit: ")) - 1
        tasks[task_number]["name"] = input("Enter new task name: ")
        tasks[task_number]["description"] = input("Enter new task description: ")
        print("Task updated successfully!")
    except (IndexError, ValueError):
        print("Invalid task number!")
def delete_task():
    display_tasks()
    try:
        task_number = int(input("\nEnter the task number to delete: ")) - 1
        tasks.pop(task_number)
        print("Task deleted successfully!")
    except (IndexError, ValueError):
        print("Invalid task number!")
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Toggle task status")
        print("4. Edit task")
        print("5. Delete task")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            toggle_task_status()
        elif choice == "4":
            edit_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()
