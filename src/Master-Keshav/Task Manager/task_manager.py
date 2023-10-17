import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.categories = set()

    def add_task(self, category, description, due_date):
        task = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'category': category,
            'description': description,
            'due_date': due_date,
            'completed': False,
        }
        self.tasks.append(task)
        self.categories.add(category)

    def update_task(self, task_index, description, due_date):
        if task_index < 0 or task_index >= len(self.tasks):
            print("Invalid task index.")
            return

        task = self.tasks[task_index]
        task['description'] = description
        task['due_date'] = due_date

    def complete_task(self, task_index):
        if task_index < 0 or task_index >= len(self.tasks):
            print("Invalid task index.")
            return

        task = self.tasks[task_index]
        task['completed'] = True

    def view_tasks(self):
        for index, task in enumerate(self.tasks):
            status = "Completed" if task['completed'] else "Incomplete"
            print(f"{index + 1}. ({status}) Category: {task['category']}, Description: {task['description']}, Due Date: {task['due_date']}")

    def view_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task['completed']]
        if completed_tasks:
            print("Completed Tasks:")
            for task in completed_tasks:
                print(f"Category: {task['category']}, Description: {task['description']}, Due Date: {task['due_date']}")
        else:
            print("No completed tasks found.")

    def view_overdue_tasks(self):
        today = datetime.now()
        overdue_tasks = [task for task in self.tasks if not task['completed'] and task['due_date'] and today > datetime.strptime(task['due_date'], "%Y-%m-%d")]
        if overdue_tasks:
            print("Overdue Tasks:")
            for task in overdue_tasks:
                print(f"Category: {task['category']}, Description: {task['description']}, Due Date: {task['due_date']}")
        else:
            print("No overdue tasks found.")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.tasks, file)

    def load_tasks(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.tasks = json.load(file)
                self.categories = set(task['category'] for task in self.tasks)

def main():
    filename = "tasks.json"
    manager = TaskManager()

    if os.path.exists(filename):
        manager.load_tasks(filename)

    print("Welcome to the Task Manager!")
    while True:
        print("Options:")
        print("1. Add a task")
        print("2. Update a task")
        print("3. Complete a task")
        print("4. View tasks")
        print("5. View completed tasks")
        print("6. View overdue tasks")
        print("7. Save and exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            category = input("Enter the task category: ")
            description = input("Enter the task description: ")
            due_date = input("Enter the due date (optional - format: YYYY-MM-DD): ")
            manager.add_task(category, description, due_date)
        elif choice == '2':
            task_index = int(input("Enter the task index to update: ")) - 1
            description = input("Enter the updated task description: ")
            due_date = input("Enter the updated due date (optional - format: YYYY-MM-DD): ")
            manager.update_task(task_index, description, due_date)
        elif choice == '3':
            task_index = int(input("Enter the task index to mark as completed: ")) - 1
            manager.complete_task(task_index)
        elif choice == '4':
            manager.view_tasks()
        elif choice == '5':
            manager.view_completed_tasks()
        elif choice == '6':
            manager.view_overdue_tasks()
        elif choice == '7':
            manager.save_tasks(filename)
            break

if __name__ == "__main__":
    main()
