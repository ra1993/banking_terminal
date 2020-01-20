def get_option():
    print()
    print("Please choose an option")
    return option

def get_account():
    print()
    print("Enter account number:")
    return input()

def show_homemenu(option):
    get_account()
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")

def show_mainmenu(option):

    print(f"Hello. Please choose an option: {option}")
    print("1. Create an account")
    print("2. Login")
    print("3. Exit Terminal")

    if option == "2":
        show_loginmenu(option)


def get_input():
    return input("Your choice: ")

def bad_input():
    print("Invalid Input")
