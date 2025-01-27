import csv # importing CSV module for file handling

# Define the add_transaction function
def add_transaction(transactions):
    """Add a new transaction to the list."""
    print("\nAdding a new transaction:")
    date = input("Date (MM-DD-YYYY): ")
    category = input("Category (e.g., Food, Rent, Salary): ")
    description = input("Description: ")

    # Validate amount
    while True:
        try:
            amount = float(input("Amount ($): "))
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    # Validate transaction type
    while True:
        transaction_type = input("Type (Income/Expense): ").capitalize()
        if transaction_type in ["Income", "Expense"]:
            break
        else:
            print("Invalid type. Please enter 'Income' or 'Expense'.")

    # Append the transaction
    transactions.append({
        "Date": date,
        "Category": category,
        "Description": description,  # This matches the 'Description' key in fieldnames
        "Amount": amount,
        "Type": transaction_type
    })
    print("Transaction added successfully!\n")


# Define the view_transactions function
def view_transactions(transactions):
    """Display all transactions in a readable format."""
    print("\nSummary of Transactions:")
    if transactions:
        for transaction in transactions:
            print(f"{transaction['Date']}: {transaction['Type']} of ${transaction['Amount']} "
                  f"in {transaction['Category']} ({transaction['Description']})")
    else:
        print("No transactions to display.")

def save_transactions_to_file(transactions, filename="transactions.csv"):
    """Save all transactions to a CSV file."""
    # Ensure the fieldnames match the transaction dictionary keys
    fieldnames = ["Date", "Category", "Description", "Amount", "Type"]
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Write the header row
        writer.writerows(transactions)  # Write all transaction rows
    print(f"Transactions saved to {filename}.\n")

#delete
def delete_transaction(transactions):
    #delete transaction by its index
    if not transactions:
        print("\nNo transactions avaliable to delete")
        return

    # display  transaction with index
    print("\nTransactions:")
    for i, transaction in enumerate(transactions, start=1):
        print(f"{i}. {transaction['Date']}: {transaction['Type']} of ${transaction['Amount']} "
              f"in {transaction['Category']} ({transaction['Description']})")

    # ask the user to choose a transaction to delete 
    while True:
        try:
            index = int(input("\nEnter the number of the transaction to delete (or 0 to cancel): "))
            if index == 0:
                print("Deletion cancelled")
                return
            if 1 <= index <= len(transactions):
                #delete the selected transaction
                deleted = transactions.pop(index - 1)
                print(f"Deleted transaction: {deleted['Date']} - {deleted['Type']} of ${deleted['Amount']} "
                      f"in {deleted['Category']} ({deleted['Description']})\n")
                return
            else: 
                print(f"Invalid code choose a number between 1 and {len(transactions)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number")

# search transactions
def search_transactions(transactions):
    if not transactions:
        print("\nNo Transactions avaliable to search")
        return
    print("\nSearh by:")
    print("1. Date (MM-DD-YYYY)")
    print("2. Category (e.g., Food, Rent, Salary)")
    print("3. Type (Income/Expense)")
    choice = input("Choose a search option (1-3:): ")

    if choice == "1":
        search_date = input("Enter the date (MM-DD-YYYY): ")
        results = [t for t in transactions if t["Date"] == search_date]
    elif choice == "2":
        search_category = input("Enter the category (e.g., Food, Rent, Salary,): ").capitalize()
        results = [t for t in transactions if t["Category"] == search_category]
    elif choice == "3":
        search_type = input("Enter the type (Income/Expense): ").capitalize()
        results = [t for t in transactions if t["Type"] == search_type]
    else:
        print("Invalid choice returning to menu")
        return

# Display search results
    print("\nSearch Results:")
    if results:
        for transaction in results:
            print(f"{transaction['Date']}: {transaction['Type']} of ${transaction['Amount']} "
                  f"in {transaction['Category']} ({transaction['Description']})")
    else:
        print("No transactions match your search criteria.")


#define load_transactions_from_file
def load_transactions_from_file(filename="transactions.csv"):
    transactions = []
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                #convert Amount to float
                row["Amount"] = float(row["Amount"])
                transactions.append(row)
        print(f"Transactions loaded from {filename}.\n")
    except FileNotFoundError:
        print(f"No existing transaction file found. Starting fresh\n")
    return transactions

def view_summary_stats(transactions):
    #display summary stats
    if not transactions:
        print("\nNo transaction available for stats")
        return

    #calculate tools 
    total_income = sum(t["Amount"] for t in transactions if t["Type"] == "Income")
    total_expenses = sum(t["Amount"] for t in transactions if t["Type"] == "Expense")
    net_balance = total_income - total_expenses
    # find largest and smallest transactions
    largest_transaction = max(transactions, key=lambda t: t["Amount"], default=None)
    smallest_transaction = min(transactions, key=lambda t: t["Amount"], default=None)

    #Dispaly stats 
    print("\nSummary Stats:")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Balance: ${net_balance:.2f}")
    if largest_transaction:
        print(f"Largest Transaction: {largest_transaction['Date']} - {largest_transaction['Type']} of "
              f"${largest_transaction['Amount']} in {largest_transaction['Category']} "
              f"({largest_transaction['Description']})")
    if smallest_transaction:
        print(f"Smallest Transaction: {smallest_transaction['Date']} - {smallest_transaction['Type']} of "
              f"${smallest_transaction['Amount']} in {smallest_transaction['Category']} "
              f"({smallest_transaction['Description']})")
# Main function with menu
def main():
    print("Welcome to your Personal Finance Dashboard!\n")

    # load transaction from file
    transactions = load_transactions_from_file()

    while True:
            print("\nMenu:")
            print("1. Add New Transaction")
            print("2. View All Transactions")
            print("3. Save Transactions")
            print("4. Delete Transaction")
            print("5. Search Transaction")
            print("6. View Summary Stats")
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
                search_transactions(transactions)  # Call the search function
            elif choice == "6":
                view_summary_stats(transactions)
            elif choice == "7":
            # Save before exiting
                save_transactions_to_file(transactions)
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
