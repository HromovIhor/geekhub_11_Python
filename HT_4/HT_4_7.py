"""
Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому
"""

def repeat(list):
    dict = {i:list.count(i) for i in list}
    print(dict)

some_list = (input("Enter any values like - 1, 2, a, b, etc.):\n")).split(sep=", ")
repeat(some_list)
