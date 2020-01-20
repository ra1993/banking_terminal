import model
import view

def run():
    option = view.get_option()
    mainmenu(option)

    account = view.get_account()
    loginmenu(account)


def mainmenu(option):

    while True:
        view.show_mainmenu(option)
        selection = view.get_input()
        

        if selection == "3":
            return
        elif selection == "1":
            model.create_account(account)

def loginmenu(account):
    
    view.show_loginmenu(account)
    selection = view.get_input()

    if selection == "4":
        return
    elif selection == "1":


if __name__ == "__main__":
    run()

        


    

    

    



        