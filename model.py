import json

def load():
    with open('accountdata.json', 'r') as f_object:
        data = json.load(f_object)
    return data

def save(data):
    with open('accountdata.json', 'w') as f_object:
        json.dump(data, f_object, indent=2)


def create_account():
    data = load()
    account = input("Please provide a new account number")
    while not account.isnumeric():
        account = input("That account number contains non-numeric entries, please numbers only!")
    data[account] = {"balance": []}
    save(data)

def deposit(account):
    data = load()
    amount = input("Enter the amount you'd like to deposit")
    data[account]["balance"].append(float(amount))
    save(data)

def withdraw(account):
    data = load()
    data[account]["balance"]
    withdrawl = input("How much would you like to withdraw?")
    new_balance = data[account]["balance"] - withdrawl

    if withdrawl > balance:
        print("Error, invalid amount requested.")

    save(data)

def get_balance(account):
    data = load()
    balance = data[account]["balance"]
    # TODO: add error handling for len == 0
    return sum(float(balance))