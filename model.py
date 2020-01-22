import json

def load():         #loads file
    with open('accountdata.json', 'r') as f_object:
        data = json.load(f_object)
    return data

def save(data):     #saves file
    with open('accountdata.json', 'w') as f_object:
        json.dump(data, f_object, indent=2)

def create_account():   #create account
    data = load()
    account = input("Please provide a new account number")
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    pin_num = input("Please enter a numerical pin number ")
    while not account.isnumeric():
        print("Account is a number")
        account = input("That account number contains non-numeric entries, please numbers only!")
        # data[account]["First_name"] = first_name
        # data[account]["Last Name"] = last_name
        # data[account]["Pin Num"] = pin_num
        #data[account]["balance"] = []
    data[account]={"balance":[], "First_name":first_name, "Last_name": last_name, "pin_num":pin_num}
   # print(data)
    #print(first_name, last_name, pin_num)
    option = input("Would you like to deposit $25? Y/N")
    if option == "Y" or option == "y":
            data[account] = {"balance": 25}
    elif option == "N" or option == "n":
        save(data)
    save(data)


def deposit(account):
    data = load()
    amount = input("Enter the amount you'd like to deposit")
    current_balance = float(data[account]["balance"])
    current_balance += float(amount)
    data[account]["balance"] = current_balance
    save(data)

def withdraw(account):
    data = load()
    current_balance = float(data[account]["balance"])
    withdrawl = float(input("How much would you like to withdraw?"))
    if withdrawl > current_balance:
        print("Error, you will overdraft your account!")
    else:
        current_balance -= withdrawl
    data[account]["balance"] = current_balance
    save(data)

def balance(account):
    data = load()
    current_balance = data[account]["balance"]
    print("Your account balance is: ", float(current_balance))
    print("-------------------------------------------")
    

#add in other account creation details. 
#work on withdraw function      done
#work on balance function       done
#add in a pin number
#prompt to deposit 25 for accont creation    done