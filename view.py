import model

def get_option():                   #recieves input from user
    print()
    print("Please choose an option")
    return option

def get_account():                  #prompts user for account number
    print()
    print("Enter account number:")
    return input()

def show_loginmenu():               #When the user logs in, and is prompted what todo
  account = input('Enter Account #: ')
  pin_num = input("Enter Pin #: ")
  # check if account number is in the json file
  if not account.isnumeric():
    print("Invalid input. Account Number must have numeric values")
    return
    if not pin_num.isnumeric():
        print("Invalid input. Pin # must have numeric values!")
        return
  data = model.load()
  if account in data and pin_num in data[account]["pin_num"]: #checks account num and pin number in data
    print("Please choose an option:")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")
    option = input()
    while option not in ['1', '2', '3', '4']:
      option = input("Sorry, that's an invalid option! Please choose 1, 2 or 3: ")

    if option == '1':
      model.withdraw(account)
    elif option == '2':
      model.deposit(account)
    elif option == '3':
      model.balance(account)
    elif option == '4':
      return


def show_mainmenu():            #first user prompt

    print("Hello. Please choose an option:")
    print("1. Create an account")
    print("2. Login")
    print("3. Exit Terminal")

    option = input()
    while option not in ['1', '2', '3']:
        option = input("Sorry, invalid input. Try again.")
    return option

def get_input():
    return input("Your choice: ")

def bad_input():
    print("Invalid Input")
