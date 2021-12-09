import csv
import json


def start():
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))

    login(username, password)

    if login(username, password):
        menu(username)
    else:
        print("Incorrect data")
        exit()


def login(username, password):
    with open("users.data", "r") as f:
        reader = csv.reader(f)

        for row in reader:
            if username == row[0] and password == row[1]:
                return True


def menu(username):
    print("\t\t\t\tWelcome")
    print("Your Bank is glad to see you and your card:)")
    print("*" * 44)
    print("\n\t\t\tSELECT ACTION\n\n1 - Balance Check\n2 - Withdrawal/Deposit\n3 - Exit")

    answer = int(input("Please specify the number of the action?\n"))
    if answer == 1:
        def balance_check():
            filename = "%s_balance.data" % username
            f = open(filename, 'r')
            result = f.read()
            print("Your balance is: ", result)
            f.close()
            selection = int(input("Do you want to continue with another transaction? \n1 - YES\n2 - NO \n"))
            if selection == 1:
                menu(username)
            else:
                print("Please take your ATM Card")
                exit()

        balance_check()

    elif answer == 2:
        def deposit_withdrawal():
            add = int(input("How much do you want to deposit? To withdrawal specify the negative number with(-): "))
            filename_balance = "%s_balance.data" % username
            f = open(filename_balance, 'r')
            balance = int(f.read())
            result = balance + add
            if result < 0:
                print("Limit exceeded")
                selection = int(input("Do you want to continue with another transaction? \n1 - YES\n2 - NO \n"))
                if selection == 1:
                    deposit_withdrawal()
                else:
                    menu(username)
                f = open(filename_balance, 'w')
                f.write(str(result))
                f.close()

            filename_transaction = "%s_transactions.data" % username

            if add >= 0:
                text = "Money deposited"
            else:
                text = "Money withdrawn"

            dictionary = {text: add}
            dict_json = json.dumps(dictionary)
            encoded_json = str(json.loads(dict_json))
            f = open(filename_transaction, 'a')
            f.write(f'\n{encoded_json}')
            f.close()
            print("Your balance was successfully changed")
            selection = int(input("Do you want to continue with another transaction? \n1 - YES\n2 - NO \n"))
            if selection == 1:
                menu(username)
            else:
                print("Please take your ATM Card")
                exit()

        deposit_withdrawal()

    elif answer == 3:
        print("\t\t\t********")
        print("\t\t\tGood Bye")
        print("\t\t\t********")
        print("Don't forget to take your ATM Card")
        print("*" * 34)
        exit()
    else:
        print("This service is not available")
        exit()


start()
