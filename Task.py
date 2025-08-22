# Simple To-Do List App

tasks = []

def show_menu():
    print("\n=== To-Do List Menu ===")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print(f"Task '{task}' added successfully!")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter task number to delete: "))
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' deleted successfully!")
            except (ValueError, IndexError):
                print("Invalid task number!")

    elif choice == "4":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1-4.")
