import json
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = set()

    def add_expense(self, category, amount, description):
        expense = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'category': category,
            'amount': amount,
            'description': description,
        }
        self.expenses.append(expense)
        self.categories.add(category)

    def view_expenses(self):
        for expense in self.expenses:
            print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: ${expense['amount']}, Description: {expense['description']}")

    def get_expense_by_category(self, category):
        category_expenses = [expense for expense in self.expenses if expense['category'] == category]
        total = sum(expense['amount'] for expense in category_expenses)
        return category_expenses, total

    def view_expense_by_category(self, category):
        category_expenses, total = self.get_expense_by_category(category)
        if not category_expenses:
            print(f"No expenses found in the '{category}' category.")
        else:
            for expense in category_expenses:
                print(f"Date: {expense['date']}, Amount: ${expense['amount']}, Description: {expense['description']}")
            print(f"Total spending in '{category}': ${total}")

    def save_expenses(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.expenses, file)

    def load_expenses(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.expenses = json.load(file)
                self.categories = set(expense['category'] for expense in self.expenses)

def main():
    filename = "expenses.json"
    tracker = ExpenseTracker()

    if os.path.exists(filename):
        tracker.load_expenses(filename)

    print("Welcome to the Expense Tracker!")
    while True:
        print("Options:")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. View expenses by category")
        print("4. Save and exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            category = input("Enter the expense category: ")
            amount = float(input("Enter the expense amount: $"))
            description = input("Enter a description: ")
            tracker.add_expense(category, amount, description)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            category = input("Enter the category to view expenses: ")
            tracker.view_expense_by_category(category)
        elif choice == '4':
            tracker.save_expenses(filename)
            break

if __name__ == "__main__":
    main()
