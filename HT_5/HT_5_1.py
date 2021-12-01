"""
Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
Функція повинна приймати три аргументи:
два - обов'язкових (<username> та <password>)
і
третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
Логіка наступна:
    якщо введено коректну пару ім'я/пароль - вертається <True>;
    якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>,
    інакше (<silent> == <False>) - породжується виключення LoginException
"""

class LoginException(Exception):
    pass

def login(username, password, silent=False):
    users = [["admin1", "1q2w3e"], ["user_2", "passworD7890"], ["G_H", "student08"], ["antony", "qwerty12345"], ["dark_master", "hell_666"]]
      
    for user in users:
        if user[0] == username and user[1] == password:
            return True

    if silent is True:
        return False
    else:
        raise LoginException
        
login(input("Username: "), input("Password: "), input("Silent can be:\nTrue\nFalse\nor leave it empty:)\nWhat's it gonna be? "))
