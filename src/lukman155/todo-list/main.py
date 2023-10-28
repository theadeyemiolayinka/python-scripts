class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def view_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("Your to-do list is empty.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task}' removed from the to-do list.")
        else:
            print("Invalid task index. Please enter a valid task number.")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            to_do_list.add_task(task)
        elif choice == "2":
            to_do_list.view_tasks()
        elif choice == "3":
            to_do_list.view_tasks()
            task_index = int(input("Enter the task number to remove: "))
            to_do_list.remove_task(task_index)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
