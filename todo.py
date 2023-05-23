def show_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def add_task():
    task = input("Enter a task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added succesfully.")

def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}.{task.strip()}")
        else:
            print("No tasks found.")

def delete_task():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}.{task.strip()}")

            task_number = int(input("Enter the task number to delete:"))
            if 1 <= task_number <= len(tasks):
                del tasks[task_number - 1]
                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)
                print("Task deleted succesfully.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks found.")

while True:
    show_menu()
    choice = input("Enter your choice (1-4):")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid coice. Please try again.")