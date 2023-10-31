import os

# Define the filename for the ledger
ledger_filename = "ledger.txt"

# Function to display the current balance
def view_balance():
    with open(ledger_filename, "r") as file:
        balance = float(file.read())
    print(f"Your current balance is ${balance:.2f}")

# Function to record a debit (withdrawal)
def record_debit():
    amount = float(input("How much is the debit? $"))
    with open(ledger_filename, "r") as file:
        balance = float(file.read())
    balance -= amount
    with open(ledger_filename, "w") as file:
        file.write(str(balance))
    print(f"${amount:.2f} has been debited from your account.")
    view_balance()

# Function to record a credit (deposit)
def record_credit():
    amount = float(input("How much is the credit? $"))
    with open(ledger_filename, "r") as file:
        balance = float(file.read())
    balance += amount
    with open(ledger_filename, "w") as file:
        file.write(str(balance))
    print(f"${amount:.2f} has been credited to your account.")
    view_balance()

# Main function to run the application
def main():
    # Check if the ledger file exists, create it if not
    if not os.path.exists(ledger_filename):
        with open(ledger_filename, "w") as file:
            file.write("0.00")

    print("~~~ Welcome to your terminal checkbook! ~~~")
    while True:
        print("\nWhat would you like to do?\n")
        print("1) View current balance")
        print("2) Record a debit (withdraw)")
        print("3) Record a credit (deposit)")
        print("4) Exit")

        choice = input("\nYour choice? ")
        if choice == "1":
            view_balance()
        elif choice == "2":
            record_debit()
        elif choice == "3":
            record_credit()
        elif choice == "4":
            print("Thanks, have a great day!")
            break
        else:
            print("Invalid choice: " + choice)

if __name__ == "__main__":
    main()
