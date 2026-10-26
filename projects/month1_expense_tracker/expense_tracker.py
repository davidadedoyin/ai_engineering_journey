import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("expenses.json")


def load_expenses():
    """Load the expense list from disk. If the file is absent, return an empty list."""
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_expenses(expenses):
    """Write the expense list to disk."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=2)


def add_expense(description, category, amount):
    """Create a new expense item and return it."""
    expense = {
        "description": description,
        "category": category,
        "amount": float(amount),
    }
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    return expense


def total_expenses(expenses):
    """Return the combined total of all expenses."""
    return sum(float(item["amount"]) for item in expenses)


def category_totals(expenses):
    """Return a dictionary of category names to totals."""
    totals = {}
    for item in expenses:
        category = item["category"]
        totals[category] = totals.get(category, 0.0) + float(item["amount"])
    return totals


def show_menu():
    """Print the user menu."""
    print("Expense Tracker")
    print("1) Add expense")
    print("2) View totals")
    print("3) Show category summary")
    print("4) Exit")


def main():
    """Run the command-line expense tracker."""
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Description: ")
            category = input("Category: ")
            amount = float(input("Amount: "))
            add_expense(description, category, amount)
            print("Expense saved.")
        elif choice == "2":
            expenses = load_expenses()
            print(f"Total spent: ${total_expenses(expenses):.2f}")
        elif choice == "3":
            expenses = load_expenses()
            summary = category_totals(expenses)
            for category, total in summary.items():
                print(f"{category}: ${total:.2f}")
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Please choose a valid option.")


if __name__ == "__main__":
    main()
