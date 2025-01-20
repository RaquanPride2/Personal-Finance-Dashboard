def main():
    print("Welcome to your dashboard!\n")

    # Placeholder for storing transactions
    transactions = []

    # Input loop for user transactions
    while True:
        print("Enter a new transaction (or type 'done' to finish):")
        date = input("Date (MM-DD-YYYY): ")
        if date.lower() == 'done':
            break  # Exit the loop if user is done

        # Get other transaction details
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

        # Append the transaction to the list
        transactions.append({
            "Date": date,
            "Category": category,
            "Description": description,
            "Amount": amount,
            "Type": transaction_type
        })
        print("Transaction added successfully!\n")

    # Display the summary of all transactions
    print("\nSummary of Transactions:")
    if transactions:
        for transaction in transactions:
            print(f"{transaction['Date']}: {transaction['Type']} of ${transaction['Amount']} "
                  f"in {transaction['Category']} ({transaction['Description']})")
    else:
        print("No transactions to display.")

if __name__ == "__main__":
    main()
