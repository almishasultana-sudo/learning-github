tasks = []

def show_menu():
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!")
def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
def remove_task():
    view_tasks()
    task_num = int(input("Enter task number to remove: "))
    if 0 < task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        print(f"Removed: {removed}")
    else:
        print("Invalid task number")
while True:
    show_menu()
    choice = input("Choose option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
