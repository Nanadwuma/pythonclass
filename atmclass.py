WITHDRAWAL_LIMIT = 5000

class ATM:
   
    def __init__(self):
        self.bank_accounts = [
            {"account_number": 444555,
             "pin": 4242,
             "name": "Ama Heta",
             "account_types": {
                "acc_savings": 100,
                "acc_other": 5640,
                "acc_USD": 520,
            }},
            {"account_number": 112233,
             "pin": 1221,
             "name": "John Doe",
             "account_types": {
                "acc_savings": 60000,
                "acc_other": 3000,
                "acc_USD": 1000,
            }},
        ]
    
    def show_message(self, message):
        print(f"\n{message}\n")
    
    def verify_account(self, acc_num):
        for bank_acc in self.bank_accounts:
            if int(acc_num) == bank_acc["account_number"]:
                return bank_acc
        return None
    
    def get_username(self, acc_details):
        if acc_details:
            return acc_details["name"]
        else:
            return "Please provide the correct account number"
    
    def get_acc_type(self, account, user_input):
        match int(user_input):
            case 1:
                return account["account_types"]["acc_savings"]
            case 2:
                return account["account_types"]["acc_other"]
            case 3:
                return account["account_types"]["acc_USD"]
            case 4:
                self.show_message("Exiting...")
                exit()
            case _:
                return self.show_message("Wrong Input")
    
    def verify_pin(self, acc_details, pin):
        return acc_details["pin"] == int(pin)
    
    def withdrawal(self, amount, acc_type_value):
        if amount <= self.WITHDRAWAL_LIMIT:
            result = acc_type_value - amount
            return result
        else:
            self.show_message("Exceeded withdrawal limit")
    
    def deposit(self, amount, acc_type_value):
        result = acc_type_value + amount
        return result
    
    def transaction_output(self, user_input_option, user_input_amount, user_input_pin, acc_type_value):
        user_input = int(user_input_option)
        amount = int(user_input_amount)

        if self.verify_pin(self.verified_acc, user_input_pin):
            match user_input:
                case 1:
                    return self.withdrawal(amount, acc_type_value)
                case 2:
                    return self.deposit(amount, acc_type_value)
                case 3:
                    return acc_type_value
                case 4:
                    self.show_message("Exiting...")
                    exit()
                case _:
                    return self.show_message("Wrong Input")
        else:
            return "Wrong Pin"

    def main(self):
        self.show_message("Welcome to DnD Bank Ltd")
        user_input = input("Enter Account Number: ")
        self.verified_acc = self.verify_account(user_input)
        
        if not self.verified_acc:
            self.show_message("Account number not found.")
            return

        self.show_message(f"Hello {self.get_username(self.verified_acc)}")
        acc_type_prompt_msg = """ 
        How may we help you today? Please select the Account Type:
        1. Savings
        2. Other
        3. USD
        4. Exit
        """
        self.show_message(acc_type_prompt_msg)
        user_input = input("Option: ")
        self.acc_type_value = self.get_acc_type(self.verified_acc, user_input)
        
        transaction_prompt_msg = """ 
        How may we help you today? Please select an option:
        1. Withdraw
        2. Deposit
        3. Check Balance
        4. Exit
        """
        self.show_message(transaction_prompt_msg)
        user_input_option = input("Select transaction: ")
        user_input_amount = input("Enter Amount: ")
        user_input_pin = input("Enter Pin: ")

        self.show_message(f"Available Balance: {self.transaction_output(user_input_option, user_input_amount, user_input_pin, self.acc_type_value)}")

if __name__ == "__main__":
    atm = ATM()
    atm.main()
