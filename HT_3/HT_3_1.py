# 1. Створити цикл від 0 до ... (вводиться користувачем). В циклі створити умову, яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0.

def current_value(number):
    for i in range(1, number):
        if i%17 == 0:
            print(i)

user_number = int(input("Specify your number please: "))
current_value(user_number)
