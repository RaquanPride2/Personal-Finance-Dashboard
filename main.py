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
            print("4. Exit")
            choice = input("Choose an option (1-4): ")

            if choice == "1":
                add_transaction(transactions)
            elif choice == "2":
                view_transactions(transactions)
            elif choice == "3":
                save_transactions_to_file(transactions)
            elif choice == "4":
            # save before closing
                save_transactions_to_file(transactions)
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
