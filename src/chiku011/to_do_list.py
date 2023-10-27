def main():
    task_list = load_tasks()
    
    while True:
        print("To-Do List:")
        print_tasks(task_list)
        print("\nOptions:")
        print("1. Add task")
        print("2. Mark task as done")
        print("3. Remove task")
        print("4. Quit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            mark_task_as_done(task_list)
        elif choice == "3":
            remove_task(task_list)
        elif choice == "4":
            save_tasks(task_list)
            break
        else:
            print("Invalid choice. Please try again.")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
        return [task for task in tasks if task.strip() != ""]
    except FileNotFoundError:
        return []

def save_tasks(task_list):
    with open("tasks.txt", "w") as file:
        for task in task_list:
            file.write(task + "\n")

def print_tasks(task_list):
    if not task_list:
        print("No tasks.")
    else:
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

def add_task(task_list):
    task = input("Enter the task: ")
    task_list.append(task)
    print("Task added!")

def mark_task_as_done(task_list):
    print_tasks(task_list)
    task_index = int(input("Enter the number of the task you've completed: ")) - 1
    if 0 <= task_index < len(task_list):
        print(f"Marking '{task_list[task_index]}' as done.")
        task_list.pop(task_index)
    else:
        print("Invalid task number.")

def remove_task(task_list):
    print_tasks(task_list)
    task_index = int(input("Enter the number of the task to remove: ")) - 1
    if 0 <= task_index < len(task_list):
        removed_task = task_list.pop(task_index)
        print(f"Removed task: '{removed_task}'")
    else:
        print("Invalid task number.")

if __name__ == "__main__":
    main()
