import csv  # Importing CSV module for file handling

# ==========================
# FILE HANDLING FUNCTIONS
# ==========================

def save_transactions_to_file(transactions, filename="transactions.csv"):
    """Save all transactions to a CSV file."""
    if not transactions:
        print("\nNo transactions to save.")
        return

    fieldnames = ["Date", "Category", "Description", "Amount", "Type"]
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)

    print(f"Transactions saved to {filename}.\n")

def load_transactions_from_file(filename="transactions.csv"):
    """Load all transactions from a CSV file."""
    transactions = []
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["Amount"] = float(row["Amount"])
                transactions.append(row)
        print(f"Transactions loaded from {filename}.\n")
    except FileNotFoundError:
        print("No existing transaction file found. Starting fresh.")
    return transactions

# ==========================
# TRANSACTION MANAGEMENT FUNCTIONS
# ==========================

def add_transaction(transactions):
    """Add a new transaction to the list."""
    print("\nAdding a new transaction:")
    date = input("Date (MM-DD-YYYY): ")
    category = input("Category (e.g., Food, Rent, Salary): ")
    description = input("Description: ")

    while True:
        try:
            amount = float(input("Amount ($): "))
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    while True:
        transaction_type = input("Type (Income/Expense): ").capitalize()
        if transaction_type in ["Income", "Expense"]:
            break
        else:
            print("Invalid type. Please enter 'Income' or 'Expense'.")

    transactions.append({
        "Date": date,
        "Category": category,
        "Description": description,
        "Amount": amount,
        "Type": transaction_type
    })
    print("Transaction added successfully!\n")

def view_transactions(transactions):
    #Display all transactions in a readable format
    print("\nSummary of Transactions:")
    if transactions:
        for transaction in transactions:
            print(f"{transaction['Date']}: {transaction['Type']} of ${transaction['Amount']} "
                  f"in {transaction['Category']} ({transaction['Description']})")
    else:
        print("No transactions to display.")

def delete_transaction(transactions):
    #Delete a transaction by its index.#
    if not transactions:
        print("\nNo transactions available to delete.")
        return

    print("\nTransactions:")
    for i, transaction in enumerate(transactions, start=1):
        print(f"{i}. {transaction['Date']}: {transaction['Type']} of ${transaction['Amount']} "
              f"in {transaction['Category']} ({transaction['Description']})")

    while True:
        try:
            index = int(input("\nEnter the number of the transaction to delete (or 0 to cancel): "))
            if index == 0:
                print("Deletion cancelled.")
                return
            if 1 <= index <= len(transactions):
                deleted = transactions.pop(index - 1)
                print(f"Deleted transaction: {deleted['Date']} - {deleted['Type']} of ${deleted['Amount']} "
                      f"in {deleted['Category']} ({deleted['Description']})\n")
                return
            else:
                print(f"Invalid choice. Choose a number between 1 and {len(transactions)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# ==========================
# SEARCH & EXPORT FUNCTIONS
# ==========================

def export_transactions_to_file(transactions, filename="filtered_transactions.csv"):
    """Export filtered transactions to a CSV file."""
    if not transactions:
        print("\nNo transactions to export.")
        return

    fieldnames = ["Date", "Category", "Description", "Amount", "Type"]
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)

    print(f"Filtered transactions exported to {filename}.\n")

def search_transactions(transactions):
    """Search for transactions based on user-defined criteria and allow export."""
    if not transactions:
        print("\nNo transactions available to search.")
        return

    print("\nSearch by:")
    print("1. Date (MM-DD-YYYY)")
    print("2. Category (e.g., Food, Rent, Salary)")
    print("3. Type (Income/Expense)")
    choice = input("Choose a search option (1-3): ")

    filename_suffix = ""

    if choice == "1":
        search_date = input("Enter the date (MM-DD-YYYY): ")
        results = [t for t in transactions if t["Date"] == search_date]
        filename_suffix = search_date
    elif choice == "2":
        search_category = input("Enter the category: ").capitalize()
        results = [t for t in transactions if t["Category"] == search_category]
        filename_suffix = search_category.lower()
    elif choice == "3":
        search_type = input("Enter the type (Income/Expense): ").capitalize()
        results = [t for t in transactions if t["Type"] == search_type]
        filename_suffix = search_type.lower()
    else:
        print("Invalid choice. Returning to menu.")
        return

    print("\nSearch Results:")
    if results:
        for transaction in results:
            print(f"{transaction['Date']}: {transaction['Type']} of ${transaction['Amount']} "
                  f"in {transaction['Category']} ({transaction['Description']})")

        default_filename = f"transactions_{filename_suffix}.csv"
        export_choice = input("\nWould you like to export these transactions? (yes/no): ").lower()
        if export_choice == "yes":
            filename = input(f"Enter filename (default: {default_filename}): ").strip()
            if not filename:
                filename = default_filename
            export_transactions_to_file(results, filename)
    else:
        print("No transactions match your search criteria.")

# ==========================
# SUMMARY STATISTICS
# ==========================

def view_summary_statistics(transactions):
    """Display summary statistics for all transactions."""
    if not transactions:
        print("\nNo transactions available for statistics.")
        return

    total_income = sum(t["Amount"] for t in transactions if t["Type"] == "Income")
    total_expenses = sum(t["Amount"] for t in transactions if t["Type"] == "Expense")
    net_balance = total_income - total_expenses

    print("\nSummary Statistics:")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Balance: ${net_balance:.2f}")

# ==========================
# MAIN FUNCTION & MENU SYSTEM
# ==========================

def main():
    print("Welcome to your Personal Finance Dashboard!\n")
    transactions = load_transactions_from_file()

    while True:
        print("\nMenu:")
        print("1. Add a New Transaction")
        print("2. View All Transactions")
        print("3. Save Transactions")
        print("4. Delete a Transaction")
        print("5. Search Transactions")
        print("6. View Summary Statistics")
        print("7. Exit")
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            save_transactions_to_file(transactions)
        elif choice == "4":
            delete_transaction(transactions)
        elif choice == "5":
            search_transactions(transactions)
        elif choice == "6":
            view_summary_statistics(transactions)
        elif choice == "7":
            save_transactions_to_file(transactions)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
