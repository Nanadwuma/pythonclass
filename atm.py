print("Welcome to DnD Bank Gh Ltd")

class Account:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount} successfully. New balance: {self.balance}"
        else:
            return "Invalid amount."

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn {amount} successfully. New balance: {self.balance}"
        else:
            return "Insufficient funds."

    def check_balance(self):
        return f"Available balance: {self.balance}"
    

# First enter account number. welcome mesage appears after entering acc number
account_mapping = {100150555: "Nana", 100150666: "Mawu", 100150600: "Pena"}
def main():
    acc_num = int(input("Enter your account number: "))
    if acc_num in account_mapping:
        first_name = account_mapping[acc_num]
        print(f"Welcome, {first_name}!")
    else:
        print("Account number not found.")

    # first_name = input("Enter your first name: ")
    # print(f"Welcome, {first_name}!")

# Select account type
    savings_account = Account("Savings", account_number=100150555, balance=53000)
    current_account = Account("Current", account_number=100150556, balance=152000)

    print("\nSelect Account:")
    print("1. Savings Account")
    print("2. Current Account")

    account_choice = int(input("Select an account type (1/2): "))

    if account_choice == 1:
        selected_account = savings_account
    elif account_choice == 2:
        selected_account = current_account
    else:
        print("Invalid choice.")
        return
#
    def account_type():
        choose = input("Enter your account type: ")
    

    savings_account = Account("Savings")
    current_account = Account("Current")

    while True:
        print("\nSelect an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Quit")

        choice = int(input("Enter choice (1/2/3/4): "))

        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            account_type = input("Enter account type (savings/current): ").lower()
            account = savings_account if account_type == "savings" else current_account
            print(account.deposit(amount))

        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            account_type = input("Enter account type (savings/current): ").lower()
            account = savings_account if account_type == "savings" else current_account
            print(account.withdraw(amount))

        elif choice == 3:
            account_type = input("Enter account type (savings/current): ").lower()
            account = savings_account if account_type == "savings" else current_account
            print(account.check_balance())

        elif choice == 4:
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
#     
    print(f"\nWelcome to your {selected_account.name} account!")


    # Additional transactions
    selected_account.deposit(5000)
    selected_account.withdraw(15000)

    print("\nAfter Additional Transactions:")
    print(f"Account Number: {selected_account.account_number}")
    print(f"Account Type: {selected_account.name}")
    print("Account Balance:", selected_account.balance)

if __name__ == "__main__":
    main()
