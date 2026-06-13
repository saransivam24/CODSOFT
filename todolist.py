def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No Tasks!")
    else:
        for index, task in enumerate(tasks, 1):
            print(index, task)


def delete_task(tasks):
    task = input("Enter task to delete: ")
    tasks.remove(task)
    print("Task deleted!")

tasks = []

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")
    
    choice = input("Enter choice: ")

    if choice =="1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)    

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4":
        print("quit")
        break
    else:
        print("Invalid choice")
    
