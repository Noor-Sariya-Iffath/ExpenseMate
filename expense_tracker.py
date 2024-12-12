import json
from datetime import datetime

def load_expenses():
    try:
        with open('expenses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)

def add_expense(expenses):
    amount = float(input("Enter expense amount: "))
    description = input("Enter expense description: ")
    date = input("Enter date (YYYY-MM-DD): ")
    expenses.append({"amount": amount, "description": description, "date": date})
    save_expenses(expenses)

def view_expenses(expenses):
    print("\nExpenses:")
    for expense in expenses:
        print(f"{expense['date']}: {expense['description']} - ${expense['amount']}")

def main():
    expenses = load_expenses()
    while True:
        action = input("\nEnter 'add' to add an expense, 'view' to view expenses, or 'exit' to quit: ").strip().lower()
        
        if action == 'add':
            add_expense(expenses)
        elif action == 'view':
            view_expenses(expenses)
        elif action == 'exit':
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
