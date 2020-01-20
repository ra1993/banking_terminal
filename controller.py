import model
import view

def run():
    while True:
        selection = view.show_mainmenu()

        if selection == '1':
            model.create_account()
        elif selection == '2':
            view.show_loginmenu()
        elif selection == '3':
            exit(1)


if __name__ == "__main__":
    run()

        


    

    

    



        