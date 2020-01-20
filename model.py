import json

def load():
    with open('accountdata.json', 'r') as f_object:
        data = json.load(f_object)
    return data

def save(data):
    with open('accountdata.json', 'w') as f_object:
        json.dump(data, f_object, indent=2)


def create_account(account):
    data = load()
    print("Please enter your new account #")
    data[account] = {"balance": []}
    save(data)

def deposit(account, balance):
    data = load()
    data[account]["balance"].append(float(balance))
    save(data)

def withdraw(account, balance):
    data = load()
    data[account]["balance"]
    withdrawl = float(input("How much would you like to withdraw?"))
    new_balance = data[account]["balance"] - withdrawl

    if withdrawl > balance:
        print("Error, invalid amount requested.")

    save(data)

def get_balance(account):
    data = load()
    balance = data[account]["balance"]
    # TODO: add error handling for len == 0
    return sum(balance)