"""
На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів
      (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором:
      перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
    Name: vasya
    Password: wasd
    Status: password must have at least one digit
    -----
    Name: vasya
    Password: vasyapupkin2000
    Status: OK
P.S. Не забудьте використати блок try/except ;)
"""

class WrongLogin(Exception):
    pass

class WrongPass(Exception):
    pass

class CapsLock(Exception):
    pass

def validation():
    check = False
    users = {
            "admin1": "1q2w3e",
            "us": "password1",
            "IHOR": "student08",
            "antony": "qwerty12345",
            "dark_master": "hellyeah666"
    }

    password_list = users.values()

    for password in password_list:
        for i in password:
            if i.isdigit():
                check = True
                break

    for username in users:
        print("Login: {}".format(username))
        print("Password: {}".format(users.get(username)))

        try:
            if len(username) < 3 or len(username) > 50:
                raise WrongLogin("Username must be in 3 to 50 characters long")
            if len(users.get(username)) < 8 or check == False:
                raise WrongPass("Password must not be less than 8 characters and 1 of them must be a number!")
            if username.isupper():
                raise CapsLock("Don't SHOUT your USERNAME at ME!!!")
        except WrongLogin:
            print("Username must be in 3 to 50 characters long")
        except WrongPass:
            print("Password must not be less than 8 characters and 1 of them must be a number!")
        except CapsLock:
            print("SHOUTING IS BAD")
        else:
            print("Passed")
        finally:
            print('-'*5)

validation()
