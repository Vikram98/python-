'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import os
import json

# File to store expenses
EXPENSES_FILE = 'expenses.json'

def load_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return []
    with open(EXPENSES_FILE, 'r') as file:
        return json.load(file)

def save_expenses(expenses):
    with open(EXPENSES_FILE, 'w') as file:
        json.dump(expenses, file)

def add_expense(amount, category, description):
    expenses = load_expenses()
    expense = {'amount': amount, 'category': category, 'description': description}
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense added: {expense}")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
    else:
        print("\nExpenses:")
        for expense in expenses:
            print(f"Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(amount, category, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == '__main__':
    main()
