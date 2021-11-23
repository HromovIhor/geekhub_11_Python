# 3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)

def seasons(number):
    if number in [12, 1, 2]:
        print("Winter")
    elif 3 <= number <= 5:
        print("Spring")
    elif 6 <= number <= 8:
        print("Summer")
    elif 9 <= number <= 11:
        print("Autumn")
    else:
        print("No such month, you're drunk - go home!")

user_input_number = int(input("Which month it is in numbers? "))
seasons(user_input_number)
