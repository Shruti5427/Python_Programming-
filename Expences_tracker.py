import csv
import os
import datetime

# Define fixed categories
CATEGORIES = {
    "A": "Food",
    "B": "College",
    "C": "Extras",
    "D": "Grocery",
    "E": "Living"
}

# File to store expenses
CSV_FILE = "expenses.csv"

# Ensure CSV file exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])  # CSV Header

# Function to add multiple expenses
def add_expenses():
    try:
        num_expenses = int(input("Enter the number of expenses you want to record: ").strip())
        if num_expenses <= 0:
            print("Number of expenses must be greater than zero.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    expenses = []
    for _ in range(num_expenses):
        print("\nChoose a category:")
        for key, value in CATEGORIES.items():
            print(f"{key}. {value}")
        
        category_choice = input("Enter category letter (A-E): ").strip().upper()
        if category_choice not in CATEGORIES:
            print("Invalid category choice. Try again.")
            continue
        
        try:
            amount = float(input("Enter amount: ").strip())
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue
        
        date = datetime.date.today().strftime("%Y-%m-%d")
        expenses.append([date, CATEGORIES[category_choice], amount])
    
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(expenses)
    
    print(f"{len(expenses)} expenses added successfully!\n")

# Function to get monthly summary
def get_summary():
    total_spent = 0
    category_totals = {category: 0 for category in CATEGORIES.values()}
    
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                amount = float(row["Amount"])
                total_spent += amount
                category_totals[row["Category"]] += amount
    except (FileNotFoundError, KeyError, ValueError):
        print("No valid expenses recorded yet.")
        return
    
    print("\n===== Monthly Expense Summary =====")
    print(f"Total Spent: ${total_spent:.2f}")
    print("Category-wise spending:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")
    print("===================================\n")

# Simple CLI to interact with the expense tracker
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expenses")
        print("2. View Monthly Summary")
        print("3. Exit")
        
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expenses()
        elif choice == "2":
            get_summary()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()