"""
Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
P.S. Повинен вертатись генератор.
"""

def range_analog(start,stop,step=1):
    while start < stop:
        yield start
        start += step

for n in range_analog(1,37,4):
    print(n)
