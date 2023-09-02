print("Welcome to DnD Bank Gh Ltd!")

class Account:
    def __init__(self, first_name, balance = 15023.25, pin = 1234):
        self.first_name = first_name
        self.balance = balance
        self.pin = pin

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

    def validate_pin(self, entered_pin):
        return self.pin == entered_pin


def main():
    account_number = 100111
    first_name = "Nana"
    pin = "1234"  

    account = Account(first_name, pin=pin)

    entered_account_number = int(input("Enter your account number: "))

    if entered_account_number != account_number:
        print("Account number not found.")
        return

    print(f"Welcome, {account.first_name}!")

    print("\nSelect an account type:")
    print("1. Savings Account")
    print("2. Current Account")

    account_type = int(input("Enter account type (1/2): "))

    if account_type not in [1, 2]:
        print("Invalid account type.")
        return

    entered_pin = input("Enter your 4-digit PIN: ")

    if len(entered_pin) != 4 or not entered_pin.isdigit():
        print("Invalid PIN. Please provide a 4-digit PIN.")
        return

    if not account.validate_pin(entered_pin):
        print("Invalid PIN. Enter Correct PIN.")
        return

    print("\nSelect a transaction type:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Quit")

    transaction_type = int(input("Enter transaction type (1/2/3/4): "))

    if transaction_type == 1:
        amount = float(input("Enter amount to deposit: "))
        print(account.deposit(amount))
    elif transaction_type == 2:
        amount = float(input("Enter amount to withdraw: "))
        print(account.withdraw(amount))
    elif transaction_type == 3:
        print(account.check_balance())
    elif transaction_type == 4:
        quit_confirmation = input("Are you sure you want to quit? (1/2): ").lower()
        if quit_confirmation == "1":
        #if quit_confirmation == "2":    
            print("Thanks for banking with us!")
        else:
            
            print("Transaction cancelled.")
    else:
        print("Invalid transaction type. Please select a valid option.")

    
#print("Thanks for banking with us!!!")
if __name__ == "__main__":
    main()

