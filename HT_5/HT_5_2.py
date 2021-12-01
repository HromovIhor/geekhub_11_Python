"""
Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :)
Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
"""

class WrongLogin(Exception):
    pass

class WrongPass(Exception):
    pass

class CapsLock(Exception):
    pass

def validation(username,password):
    check = False
    for i in password:
        if i.isdigit():
            check = True
            break

    if len(username) < 3 or len(username) > 50:
        raise WrongLogin("Username must be in 3 to 50 characters long")

    if len(password) < 8 or check == False:
        raise WrongPass("Password must not be less than 8 characters and 1 of them must be a number!")

    if username.isupper():
        raise CapsLock("Don't SHOUT your USERNAME at ME!!!")

validation(input("Login: "),input("Pass: "))
