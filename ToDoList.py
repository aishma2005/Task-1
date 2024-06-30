# Function to display the menu options
def display_menu():
    print("\n===== To-Do List Application =====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Quit")
    print("===============================")

# Function to display the current tasks
def view_tasks(tasks):
    print("\n===== To-Do List =====")
    if tasks:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. [{task['status']}] {task['description']}")
    else:
        print("To-Do List is empty.")
    print("========================")

# Function to add a new task
def add_task(tasks):
    description = input("Enter task to be added: ")
    tasks.append({'description': description, 'status': 'Incomplete'})
    print("Task added successfully.")

# Function to mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)
    task_idx = int(input("Enter task number to mark as complete: ")) - 1
    if 0 <= task_idx < len(tasks):
        tasks[task_idx]['status'] = 'Complete'
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_idx = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_idx < len(tasks):
        del tasks[task_idx]
        print("Task deleted.")
    else:
        print("Invalid task number.")

# Main function to run the application
tasks = []
    
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")
        
    if choice == '1':
        view_tasks(tasks)
    elif choice == '2':
        add_task(tasks)
    elif choice == '3':
        complete_task(tasks)
    elif choice == '4':
        delete_task(tasks)
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
