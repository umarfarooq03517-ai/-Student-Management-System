import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

FILE_NAME = "expenses.csv"

# Initialize CSV file
def init_file():
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])
        df.to_csv(FILE_NAME, index=False)

# Add expense
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Rent, Travel, etc.): ")
    description = input("Enter description: ")
    date_input = input("Enter date (YYYY-MM-DD) or leave blank for today: ")

    date = date_input if date_input else datetime.today().strftime('%Y-%m-%d')

    df = pd.read_csv(FILE_NAME)
    df.loc[len(df)] = [date, amount, category, description]
    df.to_csv(FILE_NAME, index=False)

    print("✅ Expense added successfully!\n")

# Load data
def load_data():
    df = pd.read_csv(FILE_NAME)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

# Summary
def show_summary(period):
    df = load_data()
    today = pd.Timestamp.today()

    if period == "daily":
        filtered = df[df["Date"].dt.date == today.date()]
    elif period == "weekly":
        filtered = df[df["Date"] >= today - pd.Timedelta(days=7)]
    elif period == "monthly":
        filtered = df[df["Date"].dt.month == today.month]

    total = filtered["Amount"].sum()
    print(f"\n📊 {period.capitalize()} Total Spending: ${total:.2f}\n")

# Top categories
def top_categories():
    df = load_data()
    category_sum = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    print("\n🔥 Top Spending Categories:")
    print(category_sum)

# Visualization
def visualize():
    df = load_data()
    category_sum = df.groupby("Category")["Amount"].sum()

    plt.figure(figsize=(12, 5))

    # Bar Chart
    plt.subplot(1, 2, 1)
    category_sum.plot(kind="bar", title="Spending by Category")
    plt.ylabel("Amount")

    # Pie Chart
    plt.subplot(1, 2, 2)
    category_sum.plot(kind="pie", autopct='%1.1f%%', title="Expense Distribution")
    plt.ylabel("")

    plt.tight_layout()
    plt.show()

# Menu
def menu():
    init_file()

    while True:
        print("\n📌 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Daily Summary")
        print("3. View Weekly Summary")
        print("4. View Monthly Summary")
        print("5. View Top Spending Categories")
        print("6. Visualize Expenses")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_summary("daily")
        elif choice == "3":
            show_summary("weekly")
        elif choice == "4":
            show_summary("monthly")
        elif choice == "5":
            top_categories()
        elif choice == "6":
            visualize()
        elif choice == "7":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    menu()
