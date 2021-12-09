"""
Програма-банкомат.
Створити програму з наступним функціоналом:
    - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
    - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
    - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
Особливості реалізації:
    - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
    - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
    - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
Особливості функціонала:
    - за кожен функціонал відповідає окрема функція;
    - основна функція - <start()> - буде в собі містити весь workflow банкомата:
    - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
    - потім - елементарне меню типа:
Введіть дію:
    1. Продивитись баланс
    2. Поповнити баланс
    3. Вихід
    - далі - фантазія і креатив :)
"""

##########################################################
username = input('Please enter your username: ')
password = input('Please enter your password: ')

def user_check():
    user_data = open('C:\\Users\\Ihor\\Desktop\\user.data', 'r')
    user_list = []
    users = user_data.read().split('\n')
    for i in range(len(users)):
        user = users[i].split(', ')
        user_list.append(user)
    return user_list


def login(username, password):
    globals()['username'] = username
    for user in users:
        if user[0] == username and user[1] == password:
            return True
    return False


def menu():
    print("\n\t\t\t\tWelcome")
    print("Your Bank is glad to see you and your card:)")
    print("*" * 44)
    print("\n\t\t\tSELECT ACTION\n\n1 - Check Balance\t\t4 - Exit\n2 - Withdrawal \n3 - Deposit")
    answer = int(input('What would you like to do?: '))


def balance():
    filename = "%s_balance.data" % username
    with open(filename) as f:
        print(f'Your balance is: {f.read()}')
    selection = int(input("Do you want to continue with another transaction? \n1 - YES\n2 - NO \n"))
    if selection == 1:
        menu()
    else:
        print("Please take your ATM Card")
        exit()

def withdraw():
    withdrawn_sum = float(input('Please enter amount you want to withdraw:\n'))
    filename = username + '_balance.data'
    trans_file = username+'_transactions.data'
    ts_file = open(trans_file,'a')
    file = open(filename,'a')
    balance = 0
    new_balance = 0
    if withdrawn_sum > balance:
        result = balance - withdrawn_sum
        print('You have insufficient balance. Your balance is:', balance)
        selection = int(input("Do you want to change the amount? \n1 - YES\n2 - NO \n"))
        if selection == 1:
            withdraw()
        elif selection == 2:
            menu()
        else:
            print("Please take your ATM Card")
            exit()
    else:
        new_balance = balance - withdrawn_sum
        new_balance = str(new_balance)

    f = open(filename, 'w')
    f.write(str(result))



def deposit():
    deposit_amount = float(input('Please enter amount to be deposited:'))
    filename = username+'.txt'
    t_filename = username+'_transactions.txt'
    transactionfile = open(t_filename,'a')
    file = open(filename,'a')
    balance = 0
    new_balance = 0
    with open(filename,'r') as file:
        for i in file:
            balance = float(i)
    with open(filename,'w+') as file2:
        new_balance = balance + deposit_amount
        new_balance = str(new_balance)
        file2.write(new_balance)
        print('Your new balance is:',new_balance)
    with open (t_filename,'a') as file3:
        balance = str(balance)
        deposit_amount = str(deposit_amount)
        file3.write('\nPrevious balance: '+balance+'. Deposit amount is:'+deposit_amount+'. New balance:'+new_balance+'\n')


def start():
    if user_check():
        while True:
            answer = menu()
            if answer == 1:
                balance()
            elif answer == 2:
                deposit()
            elif answer == 3:
                withdraw()
            elif answer == 4:
                print("\t\t\t********")
                print("\t\t\tGood Bye")
                print("\t\t\t********")
                print("Don't forget to take your ATM Card")
                print("*" * 34)
            else:
                return "This service is not available"
    return 'Bye-bye'


start()