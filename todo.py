# List to store tasks
tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index + 1}. {task['task']} - {status}")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print(f"Task '{tasks[index]['task']}' marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(index):
    if 0 <= index < len(tasks):
        task = tasks.pop(index)
        print(f"Task '{task['task']}' deleted.")
    else:
        print("Invalid task number.")
        
        
def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            try:
                index = int(input("Enter task number to complete: ")) - 1
                complete_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Exiting the app.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()