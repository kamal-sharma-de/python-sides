class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount):
        self.expenses.append({"Category": category, "Amount": amount})
        print("Expense added successfully!")

    def view_expenses(self):
        if self.expenses:
            print("Expense Tracker:")
            for idx, expense in enumerate(self.expenses, start=1):
                print(f"{idx}. Category: {expense['Category']}, Amount: ${expense['Amount']:.2f}")
        else:
            print("No expenses recorded.")

    def total_expenses(self):
        total = sum(expense['Amount'] for expense in self.expenses)
        return total

    def expenses_by_category(self):
        expenses_dict = {}
        for expense in self.expenses:
            category = expense['Category']
            amount = expense['Amount']
            if category in expenses_dict:
                expenses_dict[category] += amount
            else:
                expenses_dict[category] = amount
        return expenses_dict

def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Expenses by Category")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter the category of expense: ")
            amount = float(input("Enter the amount of expense: "))
            expense_tracker.add_expense(category, amount)
        elif choice == '2':
            expense_tracker.view_expenses()
        elif choice == '3':
            total = expense_tracker.total_expenses()
            print(f"Total Expenses: ${total:.2f}")
        elif choice == '4':
            expenses_by_category = expense_tracker.expenses_by_category()
            print("Expenses by Category:")
            for category, amount in expenses_by_category.items():
                print(f"{category}: ${amount:.2f}")
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
