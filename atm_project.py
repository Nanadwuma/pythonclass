WITHDRAWAL_LIMIT = 5000
bank_accounts = [
    
    {"account_number": 444555,
     "pin": 4242,
     "name":"Ama Heta",
     "account_types":{
        "acc_savings": 100,
        "acc_other": 5640,
        "acc_USD":520,
    }},   
    {"account_number": 112233,
     "pin": 1221,
     "name":"John Doe",
     "account_types":{
        "acc_savings": 60000,
        "acc_other": 3000,
        "acc_USD":1000,
    }},
]

# Note: 1.Show a welcome message with the user's name first name
# 1. let the user be able to withdraw, deposit, check account balance using prompts
# 2. Use a function for display messages,
# 3. Withdrawal and deposit functions should take amount

# code begin here
'''
# functions

1. account verification
2. withdrawal function
3. deposit function
4. pin verification function
5. Display message

'''
welcome_message = "Welcome to DnD Bank Ltd"
def show_message(message):
    return  print(f"\n{message}\n")
    # return message



# account verification function
def verify_account(acc_num):
    # 1. gett account number from user input, check if it exist  if not tell user to try again
    account =""
    for bank_acc in bank_accounts:
        # if bank_acc["account_number"] == int(acc_num):
        #     account = bank_acc
        if int(acc_num) == bank_acc["account_number"]:
             account = bank_acc #show_message("true")
        # else:
        #     return None #show_message("Please try again")
    return account
    # pass


show_message(welcome_message)
# take user input
user_input = input("Enter Account Number: ")
#print(type(user_input))
# print(verify_account(user_input))

verified_acc = verify_account(user_input)
# show user first name
# user_name = verified_acc["name"]

def get_username(acc_details):
    if acc_details:
        return acc_details["name"]
    else:
        return "Please provide the correct account number"

show_message(f"Hello {get_username(verified_acc)}")



acc_type_prompt_msg = """ 
How may we help you today, select Account Type
1. Savings
2. Other
3. USD
4. Exit
"""

show_message(acc_type_prompt_msg)

# take user transcation prompt

user_input = input("Option: ")


#  get the account type
def get_acc_type(account, user_input):
    # if int(user_input) == 1:
        
    match int(user_input):
        case 1:
            return account["account_types"]["acc_savings"]
        case 2:
            return account["account_types"]["acc_other"]
        case 3:
            return account["account_types"]["acc_USD"]
        case 4:
            show_message("Exiting... ")
            return exit()
        case _:
            return show_message("Wrong Input")
        



# print(get_acc_type(verified_acc, user_input))

acc_type_value = get_acc_type(verified_acc, user_input)

transaction_prompt_msg = """ 
How may we help you today, select the options below
1. Withdraw
2. Deposit
3. Check Balance
4. Exit
"""


# Verify user pin before transaction occurs
def verify_pin(acc_details, pin):
    if acc_details["pin"] == int(pin):
        return True
    else:
        return False


# withdrawal function
def withdrawal(amount):
    #  get the account tyep and subtract the amount from it
    if amount <= WITHDRAWAL_LIMIT:
        result = acc_type_value - amount
        return result
    else:
        show_message("Exceeded limit")


def deposit(amount):
    #  get the account tyep and add the amount to it    
    result = acc_type_value + amount
    return result




# print(withdrawal(6000))

# prompt the user
show_message(transaction_prompt_msg)

# return user transaction
user_input_option = input("Select transaction: ")
user_input_amount = input("Enter Amount: ")
user_input_pin = input("Enter Pin: ")


def transaction_output(user_input_option, user_input_amount, user_input_pin):
    user_input = int(user_input_option)
    amount = int(user_input_amount)

    if verify_pin(verified_acc, user_input_pin):
          
        match user_input:
            case 1:
                return withdrawal(amount)
            case 2:
                return deposit(amount)
            case 3:
                return "Balance"
            case 4:
                show_message("Exiting... ")
                return exit()
            case _:
                return show_message("Wrong Input")
    else:
        return "Wrong Pin"



show_message(f"Available Balance: {transaction_output(user_input_option, user_input_amount, user_input_pin)}")