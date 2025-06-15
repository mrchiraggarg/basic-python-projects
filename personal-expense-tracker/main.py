import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

# Create the CSV file with headers if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (e.g., food, travel, bills): ")
    amount = input("Enter amount (in ₹): ")
    
    try:
        float_amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    with open(FILENAME, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, float_amount])
    print("✅ Expense added!\n")

def view_expenses():
    print("\n--- All Expenses ---")
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            print(f"{row[0]} | {row[1]} | ₹{row[2]}")
    print()

def total_by_category():
    totals = {}
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = row[1]
            amount = float(row[2])
            if category in totals:
                totals[category] += amount
            else:
                totals[category] = amount
    print("\n--- Total by Category ---")
    for category, total in totals.items():
        print(f"{category}: ₹{total:.2f}")
    print()

def main():
    while True:
        print("=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total by Category")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
