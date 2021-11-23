# 2. Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).

def leap_years(start, end):
    for i in range(start, end + 1):
        if i % 400 == 0 or i % 4 == 0 and i % 100 != 0:
            print(i)

starting_year, ending_year = input("Set the starting year and the ending year, i.e. 1234-2021) : ").split(sep="-")

leap_years(int(starting_year), int(ending_year))
