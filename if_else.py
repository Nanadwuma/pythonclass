'''
1, get account number
2. Prompt the user
3. get user input
4. compare user input to 1st 4 character of the account number 
5. print login if true
6. if user input is last 4 tell user to nter 1st 4
5. print try again if false

'''

account_number = "1233 4563 8971 8976"
print(account_number[-4:])

user_put = "8976"
print("Enter first four digits")
user_put = input("Enter 1st 4 digits: ")
if (user_put == account_number[:4]):
    print("Login")
elif(user_put == account_number[-4:]):
    print("!Ooops, Please enter your 1st 4 digits instead")
else:
    print("Try again!")


