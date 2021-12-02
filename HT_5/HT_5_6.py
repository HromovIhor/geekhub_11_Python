"""
Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
P.S. Повинен вертатись генератор.
"""

def range_analog(start=0,stop=0,step=1):
    if stop == 0:
        stop = start
        start = 0
    while start < stop:
        yield start
        start += step
    return

test = [n for n in range_analog(10)]
print(test)

test_1 = [n for n in range_analog(5,26)]
print(test_1)

test_2 = [n for n in range_analog(5,26,2)]
print(test_2)
